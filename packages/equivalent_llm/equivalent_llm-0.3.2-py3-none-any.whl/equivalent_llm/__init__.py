import json
import itertools
import logging
import re
from typing import Optional, Union

from tqdm import tqdm

from langchain_openai import ChatOpenAI

from equivalent_llm import function_call, reservation, user
from equivalent_llm.engine.openai import OpenAI
from equivalent_llm.engine.pet import PET
from equivalent_llm.function import v1 as function_v1
from equivalent_llm.function import v2 as function_v2
from equivalent_llm.parse import json_loads

class EquvalentLLM:

    openai_configurations = {
        'temperature': 0.0,
        'model': 'gpt-4-turbo',
        'top_p': 1.0,
    }

    configurations = {
        'prompt_engine': 'PET',
        'api': 'v2',
        'llm_type': 'llama3',
        'json_warning': False,
    }

    # initialization
    instructions = []
    instruction: dict = {}
    parsed_instructions: list = []
    parsed_reference = None
    parsed_generated = None

    def __json_loads(self, json_str: str) -> dict:
        parsed = json_loads(json_str, self.configurations['json_warning'])
        #if isinstance(parsed, list) and len(parsed) == 1:
        if isinstance(parsed, list):
            return parsed[0]
        else:
            return parsed

    def __parse_preknowledge(self, preknowledge: str) -> None:
        match self.configurations['llm_type'].lower():
            case 'llama3':
                preknowledge = re.sub(r"<\|begin_of_text\|>", '', preknowledge)
                contents = preknowledge.replace('\n','').split('<|eot_id|>')[1:]
                messages = list(filter(lambda x: x is not None and x.strip() != '',
                    [
                        re.sub(r"<\|start_header_id\|>.+<\|end_header_id\|>", '', content)
                        for content in contents
                    ]))
                self.instructions = [ self.__json_loads(message) for message in messages[:-1] ]
                self.instruction = self.__json_loads(messages[-1])
                self.instructions.append(self.instruction)
            case 'llama2':
                contents = preknowledge.replace('\n','').split('</s>')
                messages = [
                    list(filter(lambda x: x is not None and x.strip() != '',
                        re.sub('.*<</SYS>>', '', content)
                        .replace('<s>[INST]', '')
                        .split('[/INST]')))
                    for content in contents
                ]
                self.instructions = list(itertools.chain([ self.__json_loads(m) for message in messages[:-1] for m in message ]))
                self.instruction = self.__json_loads(messages[-1][0])
                self.instructions.append(self.instruction)
            case 'a.x':
                contents = (
                    preknowledge
                        .replace('\n','')
                        .replace('<|endoftext|><|endoftext|>', '</|endoftext|><|endoftext|>')
                        .split('</|endoftext|>')
                )
                messages = [
                    list(filter(lambda x: x is not None and x.strip() != '',
                        re.sub('.*<</SYS>>', '', content)
                        .replace('<|endoftext|>[INST]', '')
                        .split('[/INST]')))
                    for content in contents
                ]
                self.instructions = list(itertools.chain([ self.__json_loads(m) for message in messages[:-1] for m in message ]))
                self.instruction = self.__json_loads(messages[-1][0])
                self.instructions.append(self.instruction)
            case 'mistral':
                f_region = r".*\}\]\[" # tricky
                r_region = r"["
                contents = preknowledge.replace('\n','').replace('</s>', '</s><s>').split('</s>')
                messages = [
                    list(filter(lambda x: x is not None and x.strip() != '',
                        re.sub(f_region, r_region, content)
                        .replace('<s>[INST]', '')
                        .split('[/INST]')))
                    for content in contents
                ]
                self.instructions = list(itertools.chain([ self.__json_loads(m) for message in messages[:-1] for m in message ]))
                self.instruction = self.__json_loads(messages[-1][0])
                self.instructions.append(self.instruction)
            case _:
                raise ValueError(f"Unknown LLM model type: {self.configurations['llm_type']}")

    def __init__(self, preknowledge, reference, generated, logger = None, **kwargs):
        self.preknowledge = preknowledge
        self.reference = reference
        self.generated = generated

        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.update_configurations(**kwargs)
        if self.configurations['prompt_engine'] == 'PET':
            self.prompt_engine = PET(logger=self.logger, **self.configurations)
        elif self.configurations['prompt_engine'] == 'OpenAI':
            self.update_openai_configurations(**kwargs)
            self.prompt_engine = OpenAI(logger=self.logger, **self.openai_configurations)
        else:
            raise ValueError(f"Unknown prompt engine: {self.configurations['prompt_engine']}")

        self.__parse_preknowledge(self.preknowledge)

    def update_configurations(self, **kwargs) -> None:
        self.configurations.update(kwargs)
        self.logger.debug(self.configurations)

    def update_openai_configurations(self, **kwargs) -> None:
        self.openai_configurations.update(kwargs)
        self.openai_configurations.pop('prompt_engine', None)
        self.openai_configurations.pop('api', None)
        self.openai_configurations.pop('llm_type', None)

    def parse_instructions(self) -> None:
        parsed_instructions = []
        match self.configurations['api']:
            case 'v1':
                function = function_v1
            case _:
                function = function_v2
        for index, instruction in enumerate(self.instructions):
            match instruction.get('role'):
                case 'user':
                    parsed_instructions.append(
                        user.get_entities(instruction['content'], parsed_instructions[0:index], self.prompt_engine, self.logger)
                    )
                case 'function':
                    parser = getattr(function, instruction['name'])
                    parsed_instructions.append(parser(instruction['content'], parsed_instructions[0:index], self.prompt_engine))
                case 'assistant':
                    self.logger.debug(f"Skip assistant instruction: {instruction}")
                case _:
                    raise ValueError(f"Unknown role: {instruction}")
        self.parsed_instructions = parsed_instructions
        self.logger.debug(self.parsed_instructions)

    def parse_llm(self, string: str, reference: bool = False) -> dict:
        try:
            json_parsed = json_loads(string, self.configurations['json_warning'])
            if json_parsed.get('function_call') is not None:
                # function call generation
                function = json_parsed['function_call']
                parsed = {
                    'type': 'function_call',
                    'name': function['name'],
                    'arguments': json_loads(function['arguments'], self.configurations['json_warning']),
                    'role': 'assistant',
                }
                if reference:
                    self.validation_type = 'function_call'
            else:
                # reservation generation
                status = 'valid'
                content = json_parsed['content']
                if content.endswith('###'):
                    content = content[:-3]
                doubled_content = re.findall(r'(?<=})\n?{.*', content, flags=re.DOTALL)
                if len(doubled_content) > 0:
                    content = doubled_content[-1]
                    status = 'doubled'
                parsed = {
                    'type': 'reservation',
                    'name': 'reservation',
                    'reservation': json_loads(content, self.configurations['json_warning']),
                    'status': status,
                    'role': 'assistant',
                }
                if reference:
                    self.validation_type = 'reservation'
            self.logger.debug(f"Parsing LLM: {parsed}")
            return parsed
        except json.JSONDecodeError as e:
            return { 'status': 'fail', 'error': e }


    def validate(self, **kwargs) -> dict:
        if len(self.parsed_instructions) == 0:
            self.parse_instructions()
        if self.parsed_reference is None:
            self.parsed_reference = self.parse_llm(self.reference, True)
        if self.parsed_generated is None:
            self.parsed_generated = self.parse_llm(self.generated)

        if self.parsed_reference.get('status') == 'fail':
            return {
                'target': 'Unknown',
                'passed': False,
                'count': {'passed': 0, 'total': 1},
                'status': 'fail',
                'source': 'reference',
                'raw_reference': self.reference,
                'raw_generated': self.generated,
                'error': f"Failed to parse reference (invalid JSON string): {self.parsed_reference['error']}"
            }
        if self.parsed_generated.get('status') == 'fail':
            target = 'reservation' if self.validation_type == 'reservation' else 'function call'
            return {
                'target': target,
                'passed': False,
                'count': {'passed': 0, 'total': 1},
                'status': 'fail',
                'source': 'generated',
                'reference': self.parsed_reference,
                'raw_generated': self.generated,
                'error': f"Failed to parse generated (invalid JSON string): {self.parsed_generated['error']}"
            }

        if self.validation_type == 'function_call':
            validation_reports = function_call.validate(
                self.parsed_reference['name'],
                self.parsed_generated,
                self.parsed_reference,
                self.parsed_instructions,
                self.configurations,
                self.prompt_engine,
                self.configurations['api'],
                self.logger,
            )
        else:
            validation_reports = reservation.validate(
                self.parsed_generated,
                self.parsed_reference,
                self.parsed_instructions,
                self.configurations,
                self.prompt_engine,
                self.configurations['api'],
                self.logger,
            )
        validation_reports['reference'] = self.parsed_reference
        validation_reports['generated'] = self.parsed_generated
        validation_reports['given_information'] = self.parsed_instructions
        return validation_reports


def __csv_to_list(file_path: str, encoding = 'utf-8', logger = logging.getLogger()) -> list:
    import csv

    llm_list = []
    with open(file_path, mode='r', encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                logger.info(f'Column names are {", ".join(row)}')
                line_count += 1
            llm_list.append(row)
            line_count += 1
        logger.info(f'Processed {line_count} lines.')

    return llm_list

def validate(
    llm_list: Optional[list] = None,
    csv_path: Optional[str] = None,
    columns = {
        'preknowledge': 'context',
        'reference': 'answer',
        'generated': 'generated',
    },
    indexes: Optional[Union[list, range, int]] = None,
    index: Optional[Union[list, range, int]] = None,
    print_result: bool = False,
    logger = logging.getLogger(), **kwargs
) -> dict:
    if isinstance(llm_list, str) and csv_path is None:
        csv_path = llm_list
        llm_list = None
    if llm_list is None:
        if csv_path is None:
            raise ValueError("Either llm_list or csv_path should be provided.")
        llm_list = __csv_to_list(csv_path, kwargs.get('encoding', 'utf-8'), logger)

    if indexes is None:
        indexes = index
    if isinstance(indexes, int):
        indexes = [indexes]
    elif isinstance(indexes, range):
        indexes = list(indexes)
    elif indexes is None:
        indexes = range(len(llm_list))
    llms = [llm_list[index] for index in indexes]

    validations = []
    for index, llm in tqdm(zip(indexes, llms), total = len(indexes)):
        validation = EquvalentLLM(
            llm.get(columns['preknowledge']),
            llm.get(columns['reference']),
            llm.get(columns['generated']),
            logger,
            **kwargs
        )
        validated = validation.validate()
        validated['index'] = index
        validations.append(validated)
        if print_result:
            print(validated)

    return {
        'input_data': llm_list,
        'validations': validations,
    }
