from __future__ import annotations
__all__ = [
    "HandyPrompt",
    "ChatPrompt",
    "CompletionsPrompt",
    "loads",
    "load",
    "load_from",
    "dumps",
    "dump",
    "dump_to",
    "load_var_map",
    "RunConfig",
    "RecordRequestMode",
    "CredentialType",
]

import json
import re
import copy
import io
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Union, TypeVar
from enum import auto
from abc import abstractmethod, ABC
from dataclasses import dataclass, asdict, fields, replace

import yaml
import frontmatter
from mergedeep import merge, Strategy
from dotenv import load_dotenv

from .prompt_converter import PromptConverter
from .openai_client import ClientMode, OpenAIClient
from .utils import (
    astream_chat_all, astream_completions, 
    stream_chat_all, stream_completions, 
)
from ._str_enum import AutoStrEnum


PromptType = TypeVar('PromptType', bound='HandyPrompt')
if sys.version_info >= (3, 9):
    PathType = Union[str, os.PathLike[str]]
else:
    PathType = Union[str, os.PathLike]

converter = PromptConverter()
handler = frontmatter.YAMLHandler()
p_var_map = re.compile(r'(%\w+%)')

DEFAULT_BLACKLIST = (
    "api_key", "organization", "api_base", "api_type", "api_version", 
    "endpoint_manager", "endpoint", "engine", "deployment_id", 
    "model_engine_map", "dest_url", 
)


def loads(
    text: str, 
    encoding: str = "utf-8",
    base_path: Optional[PathType] = None
) -> HandyPrompt:
    if handler.detect(text):
        metadata, content = frontmatter.parse(text, encoding, handler)
        meta = metadata.pop("meta", None) or {}
        request = metadata
    else:
        content = text
        request = {}
        meta = {}
    api: str = meta.get("api", "")
    if api:
        api = api.lower()
        if api.startswith("completion"):
            api = "completions"
        else:
            api = "chat"
    else:
        if converter.detect(content):
            api = "chat"
        else:
            api = "completions"
    if api == "completions":
        return CompletionsPrompt(content, request, meta, base_path)
    else:
        messages = converter.raw2msgs(content)
        return ChatPrompt(messages, request, meta, base_path)

def load(
    fd: io.IOBase, 
    encoding: str = "utf-8",
    base_path: Optional[PathType] = None
) -> HandyPrompt:
    text = fd.read()
    return loads(text, encoding, base_path=base_path)

def load_from(
    path: PathType,
    encoding: str = "utf-8"
) -> HandyPrompt:
    with open(path, "r", encoding=encoding) as fd:
        return load(fd, encoding, base_path=Path(path).parent.resolve())

def dumps(
    prompt: HandyPrompt, 
    base_path: Optional[PathType] = None
) -> str:
    return prompt.dumps(base_path)

def dump(
    prompt: HandyPrompt, 
    fd: io.IOBase, 
    base_path: Optional[PathType] = None
) -> None:
    return prompt.dump(fd, base_path)

def dump_to(
    prompt: HandyPrompt, 
    path: PathType
) -> None:
    return prompt.dump_to(path)

def load_var_map(path: PathType) -> dict[str, str]:
    # read all content that needs to be replaced in the prompt from a text file
    with open(path, 'r', encoding='utf-8') as fin:
        content = fin.read()
    substitute_map = {}
    blocks = p_var_map.split(content)
    for idx in range(1, len(blocks), 2):
        key = blocks[idx]
        value = blocks[idx+1]
        substitute_map[key] = value.strip()
    return substitute_map

class RecordRequestMode(AutoStrEnum):
    BLACKLIST = auto()  # record all request arguments except specified ones
    WHITELIST = auto()  # record only specified request arguments
    NONE = auto()  # record no request arguments
    ALL = auto()  # record all request arguments


class CredentialType(AutoStrEnum):
    # load environment variables from the credential file
    ENV = auto()
    # load the content of the file as request arguments
    JSON = auto()
    YAML = auto()


@dataclass
class RunConfig:
    # record request arguments
    record_request: Optional[RecordRequestMode] = None  # default: RecordRequestMode.BLACKLIST
    record_blacklist: Optional[list[str]] = None  # default: DEFAULT_BLACKLIST
    record_whitelist: Optional[list[str]] = None
    # variable map
    var_map: Optional[dict[str, str]] = None
    # variable map file path
    var_map_path: Optional[PathType] = None
    # output the result to a file or a file descriptor
    output_path: Optional[PathType] = None
    output_fd: Optional[io.IOBase] = None
    # output the evaluated prompt to a file or a file descriptor
    output_evaled_prompt_path: Optional[PathType] = None
    output_evaled_prompt_fd: Optional[io.IOBase] = None
    # credential file path
    credential_path: Optional[PathType] = None
    # credential type: env, json, yaml
    # if env, load environment variables from the credential file
    # if json or yaml, load the content of the file as request arguments
    credential_type: Optional[CredentialType] = None  # default: guess from the file extension
    
    # verbose output to stderr
    verbose: Optional[bool] = None  # default: False
    
    def __setattr__(self, name: str, value: object):
        if name == "record_request":
            # validate record_request value
            if isinstance(value, str):
                if value not in RecordRequestMode:
                    raise ValueError(f"unsupported record_request value: {value}")
            elif isinstance(value, RecordRequestMode):
                value = value.value
            elif value is None:  # this field is optional
                pass
            else:
                raise ValueError(f"unsupported record_request value: {value}")
        elif name == "credential_type":
            # validate credential_type value
            if isinstance(value, str):
                if value == 'yml':
                    value = CredentialType.YAML.value
                elif value not in CredentialType:
                    raise ValueError(f"unsupported credential_type value: {value}")
            elif isinstance(value, CredentialType):
                value = value.value
            elif value is None:  # this field is optional
                pass
            else:
                raise ValueError(f"unsupported credential_type value: {value}")
        super().__setattr__(name, value)
    
    def __len__(self):
        return len([f for f in fields(self) if getattr(self, f.name) is not None])
    
    @classmethod
    def from_dict(cls, obj: dict, base_path: Optional[PathType] = None):
        input_kwargs = {}
        for field in fields(cls):
            if field.name in obj:
                input_kwargs[field.name] = obj[field.name]
        # add base_path to path fields and convert to resolved path
        if base_path:
            for path_field in ("output_path", "output_evaled_prompt_path", "var_map_path", "credential_path"):
                if path_field in input_kwargs:
                    org_path = input_kwargs[path_field]
                    new_path = str(Path(base_path, org_path).resolve())
                    # retain trailing slash
                    if org_path.endswith(('/')):
                        new_path += '/'
                    input_kwargs[path_field] = new_path
        return cls(**input_kwargs)
    
    def pretty_print(self, file=sys.stderr):
        print("RunConfig:", file=file)
        for field in fields(self):
            value = getattr(self, field.name)
            if value is not None:
                print(f"  {field.name}: {value}", file=file)
    
    def to_dict(self, retain_fd=False, base_path: Optional[PathType] = None) -> dict:
        # record and remove file descriptors
        tmp_output_fd = self.output_fd
        tmp_output_evaled_prompt_fd = self.output_evaled_prompt_fd
        self.output_fd = None
        self.output_evaled_prompt_fd = None
        # convert to dict
        obj = asdict(self, dict_factory=lambda x: { k: v for k, v in x if v is not None })
        # restore file descriptors
        self.output_fd = tmp_output_fd
        self.output_evaled_prompt_fd = tmp_output_evaled_prompt_fd
        if retain_fd:
            # keep file descriptors
            obj["output_fd"] = self.output_fd
            obj["output_evaled_prompt_fd"] = self.output_evaled_prompt_fd
        # convert path to relative path
        if base_path:
            for path_field in ("output_path", "output_evaled_prompt_path", "var_map_path", "credential_path"):
                if path_field in obj:
                    org_path = obj[path_field]
                    try:
                        new_path = str(Path(org_path).relative_to(base_path))
                        obj[path_field] = new_path
                    except ValueError:
                        # org_path is not under base_path, keep the original path
                        pass
        return obj

    def merge(self, other: RunConfig, inplace=False) -> RunConfig:
        # merge the RunConfig object with another RunConfig object
        # return a new RunConfig object if inplace is False
        if not inplace:
            new_run_config = replace(self)
        else:
            new_run_config = self
        for field in fields(new_run_config):
            v = getattr(other, field.name)
            if v is not None:
                setattr(new_run_config, field.name, v)
        return new_run_config


DEFAULT_CONFIG = RunConfig()


class HandyPrompt(ABC):
    
    TEMPLATE_OUTPUT_FILENAME = "result.%Y%m%d-%H%M%S.hprompt"
    TEMPLATE_OUTPUT_EVAL_FILENAME = "evaled.%Y%m%d-%H%M%S.hprompt"
    
    def __init__(
        self, data: Union[str, list], request: Optional[dict] = None, 
        meta: Optional[Union[dict, RunConfig]] = None, 
        base_path: Optional[PathType] = None,
        response: Optional[dict] = None,
        ):
        self.data = data
        self.request = request or {}
        # parse meta to run_config
        if isinstance(meta, RunConfig):
            self.run_config = meta
        else:
            self.run_config = RunConfig.from_dict(meta or {}, base_path=base_path)
        self.base_path = base_path
        self.response = response
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return "{}({}, {}, {})".format(
            self.__class__.__name__,
            repr(self.data),
            repr(self.request),
            repr(self.run_config)
        )
    
    @property
    def result_str(self) -> str:
        return str(self.data)
    
    def _serialize_data(self, data) -> str:
        '''
        Serialize the data to a string. 
        This method can be overridden by subclasses.
        '''
        return str(data)
    
    @classmethod
    def _dumps_frontmatter(cls, request: dict, run_config: RunConfig, base_path: Optional[PathType] = None) -> str:
        # dump frontmatter
        if not run_config and not request:
            return ""
        # need to filter the request
        front_data = cls._filter_request(request, run_config)
        if run_config:
            front_data['meta'] = run_config.to_dict(retain_fd=False, base_path=base_path)
        post = frontmatter.Post("", None, **front_data)
        return frontmatter.dumps(post, handler).strip() + "\n\n"
    
    def dumps(self, base_path: Optional[PathType] = None) -> str:
        serialized_data = self._serialize_data(self.data)
        base_path = base_path or self.base_path
        return self._dumps_frontmatter(self.request, self.run_config, base_path) + serialized_data
    
    def dump(self, fd: io.IOBase, base_path: Optional[PathType] = None) -> None:
        text = self.dumps(base_path=base_path)
        fd.write(text)
    
    def dump_to(self, path: PathType) -> None:
        with open(path, "w", encoding="utf-8") as fd:
            self.dump(fd, base_path=Path(path).parent.resolve())
    
    @abstractmethod
    def _eval_data(self: PromptType, run_config: RunConfig) -> Union[str, list]:
        ...
    
    def eval(
        self: PromptType, 
        run_config: RunConfig = DEFAULT_CONFIG,
        **kwargs) -> PromptType:
        '''
        Evaluate the prompt with the given run_config. 
        A new prompt object is returned.
        '''
        new_run_config = self.eval_run_config(run_config)
        new_data = self._eval_data(new_run_config)
        # update the request with the keyword arguments
        evaled_request = copy.deepcopy(self.request)
        evaled_request.update(kwargs)
        return self.__class__(
            new_data,
            evaled_request,
            new_run_config,
        )
    
    def eval_run_config(
        self: PromptType, 
        run_config: RunConfig, 
        ) -> RunConfig:
        # merge runtime run_config with the original run_config
        run_config = self.run_config.merge(run_config)
        
        start_time = datetime.now()
        if run_config.output_path:
            run_config.output_path = self._prepare_output_path(
                run_config.output_path, start_time, self.TEMPLATE_OUTPUT_FILENAME
            )
        if run_config.output_evaled_prompt_path:
            run_config.output_evaled_prompt_path = self._prepare_output_path(
                run_config.output_evaled_prompt_path, start_time, 
                self.TEMPLATE_OUTPUT_EVAL_FILENAME
            )
        
        if run_config.credential_path:
            if not run_config.credential_type:
                # guess the credential type from the file extension
                p = Path(run_config.credential_path)
                if p.suffix:
                    run_config.credential_type = p.suffix[1:]
                else:
                    run_config.credential_type = CredentialType.ENV
        return run_config
    
    @classmethod
    @abstractmethod
    def _run_with_client(
        cls, 
        client: OpenAIClient, 
        evaled_prompt: PromptType,
        stream: bool,
        ) -> PromptType:
        ...
    
    def run(
        self: PromptType, 
        client: OpenAIClient = None, 
        run_config: RunConfig = DEFAULT_CONFIG,
        **kwargs) -> PromptType:
        evaled_prompt, stream = self._prepare_run(run_config, kwargs)
        if client:
            new_prompt = self._run_with_client(client, evaled_prompt, stream)
        else:
            with OpenAIClient(ClientMode.SYNC) as client:
                new_prompt = self._run_with_client(client, evaled_prompt, stream)
        self._post_check_output(stream, run_config, new_prompt)
        return new_prompt
    
    @classmethod
    @abstractmethod
    async def _arun_with_client(
        cls, 
        client: OpenAIClient, 
        evaled_prompt: PromptType,
        stream: bool,
        ) -> PromptType:
        ...
    
    async def arun(
        self: PromptType, 
        client: OpenAIClient = None, 
        run_config: RunConfig = DEFAULT_CONFIG,
        **kwargs) -> PromptType:
        evaled_prompt, stream = self._prepare_run(run_config, kwargs)
        if client:
            new_prompt = await self._arun_with_client(client, evaled_prompt, stream)
        else:
            async with OpenAIClient(ClientMode.ASYNC) as client:
                new_prompt = await self._arun_with_client(client, evaled_prompt, stream)
        self._post_check_output(stream, run_config, new_prompt)
        return new_prompt
    
    def _prepare_output_path(
        self, output_path: PathType, start_time: datetime, template_filename: str
        ) -> str:
        output_path = str(output_path).strip()
        p = Path(output_path)
        if p.is_dir() or output_path.endswith(('/')):
            # output_path wants to be a directory, append the default filename
            output_path = Path(output_path, template_filename)
        # format output_path with the current time
        output_path = start_time.strftime(str(output_path))
        # create the parent directory if it does not exist
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        return output_path
    
    def _prepare_run(self: PromptType, run_config: RunConfig, kwargs: dict):
        # evaluate the prompt with the given run_config
        evaled_prompt = self.eval(run_config=run_config, **kwargs)
        evaled_run_config = evaled_prompt.run_config
        evaled_request = evaled_prompt.request
        
        # get the stream flag
        stream = evaled_request.get("stream", False)
        
        # verbose output
        if evaled_run_config.verbose:
            print("---", file=sys.stderr)
            print("NEW RUN")
            print(f"Start time: {datetime.now()}", file=sys.stderr)
            evaled_run_config.pretty_print()
            print("---", file=sys.stderr)
        
        # output the evaluated prompt to a file or a file descriptor
        # NOTE: should be done before loading the credential file
        if evaled_run_config.output_evaled_prompt_fd:
            evaled_prompt.dump(evaled_run_config.output_evaled_prompt_fd)
        elif evaled_run_config.output_evaled_prompt_path:
            evaled_prompt.dump_to(evaled_run_config.output_evaled_prompt_path)
        
        # load the credential file
        if evaled_run_config.credential_path:
            if evaled_run_config.credential_type == CredentialType.ENV:
                load_dotenv(evaled_run_config.credential_path, override=True)
            elif evaled_run_config.credential_type in (CredentialType.JSON, CredentialType.YAML):
                with open(evaled_run_config.credential_path, 'r', encoding='utf-8') as fin:
                    if evaled_run_config.credential_type == CredentialType.JSON:
                        credential_dict = json.load(fin)
                    else:
                        credential_dict = yaml.safe_load(fin)
                # do not overwrite the existing request arguments
                for key, value in credential_dict.items():
                    if key not in evaled_request:
                        evaled_request[key] = value
            else:
                raise ValueError(f"unsupported credential type: {evaled_run_config.credential_type}")
        
        return evaled_prompt, stream
    
    def _post_check_output(self: PromptType, stream: bool, run_config: RunConfig, new_prompt: PromptType):
        if not stream:
            # if stream is True, the response is already streamed to 
            # a file or a file descriptor
            if run_config.output_fd:
                new_prompt.dump(run_config.output_fd)
            elif run_config.output_path:
                new_prompt.dump_to(run_config.output_path)
        return new_prompt

    def _merge_non_data(self: PromptType, other: PromptType, inplace=False) -> Union[None, tuple[dict, RunConfig]]:
        if inplace:
            merge(self.request, other.request, strategy=Strategy.ADDITIVE)
            self.run_config.merge(other.run_config, inplace=True)
        else:
            merged_request = merge({}, self.request, other.request, strategy=Strategy.ADDITIVE)
            merged_run_config = self.run_config.merge(other.run_config)
            return merged_request, merged_run_config
    
    @staticmethod
    def _filter_request(
        request: dict, 
        run_config: RunConfig,
        ) -> dict:
        if run_config.record_request == RecordRequestMode.WHITELIST:
            if run_config.record_whitelist:
                request = {key: value for key, value in request.items() if key in run_config.record_whitelist}
            else:
                request = {}
        elif run_config.record_request == RecordRequestMode.NONE:
            request = {}
        elif run_config.record_request == RecordRequestMode.ALL:
            pass
        else:
            # default: blacklist
            request = copy.deepcopy(request)
            real_blacklist = run_config.record_blacklist or DEFAULT_BLACKLIST
            for key in real_blacklist:
                request.pop(key, None)
        return request
    
    def _parse_var_map(self, run_config: RunConfig):
        var_map = {}
        if run_config.var_map_path:
            var_map = merge(
                var_map, 
                load_var_map(run_config.var_map_path), 
                strategy=Strategy.REPLACE
            )
        if run_config.var_map:
            var_map = merge(
                var_map, 
                run_config.var_map, 
                strategy=Strategy.REPLACE
            )
        return var_map


class ChatPrompt(HandyPrompt):
        
    def __init__(
        self, messages: list, request: dict, meta: Union[dict, RunConfig], 
        base_path: Optional[PathType] = None,
        response: Optional[dict] = None,
        ):
        super().__init__(messages, request, meta, base_path, response)
    
    @property
    def messages(self) -> list:
        return self.data
    
    @messages.setter
    def messages(self, value: list):
        self.data = value
    
    @property
    def result_str(self) -> str:
        if len(self.messages) == 0:
            return ""
        return self.messages[-1]['content']
    
    def _serialize_data(self, data) -> str:
        return converter.msgs2raw(data)
    
    def _eval_data(self, run_config: RunConfig) -> list:
        var_map = self._parse_var_map(run_config)
        return converter.msgs_replace_variables(
            self.messages, var_map, inplace=False)
    
    @classmethod
    def _run_with_client(
        cls, 
        client: OpenAIClient, 
        evaled_prompt: PromptType,
        stream: bool,
        ) -> ChatPrompt:
        run_config = evaled_prompt.run_config
        new_request = evaled_prompt.request
        response = client.chat(
            messages=evaled_prompt.data,
            **new_request
            ).call()
        base_path = Path(run_config.output_path).parent.resolve() if run_config.output_path else None
        if stream:
            if run_config.output_fd:
                # dump frontmatter, no base_path
                run_config.output_fd.write(cls._dumps_frontmatter(new_request, run_config))
                # stream response to a file descriptor
                role, content, tool_calls = converter.stream_msgs2raw(stream_chat_all(response), run_config.output_fd)
            elif run_config.output_path:
                # stream response to a file
                with open(run_config.output_path, 'w', encoding='utf-8') as fout:
                    # dump frontmatter
                    fout.write(cls._dumps_frontmatter(new_request, run_config, base_path))
                    role, content, tool_calls = converter.stream_msgs2raw(stream_chat_all(response), fout)
            else:
                role, content, tool_calls = converter.stream_msgs2raw(stream_chat_all(response))
        else:
            role = response['choices'][0]['message']['role']
            content = response['choices'][0]['message'].get('content')
            tool_calls = response['choices'][0]['message'].get('tool_calls')
        return ChatPrompt(
            [{"role": role, "content": content, "tool_calls": tool_calls}],
            new_request, run_config, base_path,
            response=response
        )
    
    @classmethod
    async def _arun_with_client(
        cls, 
        client: OpenAIClient, 
        evaled_prompt: PromptType,
        stream: bool,
        ) -> ChatPrompt:
        run_config = evaled_prompt.run_config
        new_request = evaled_prompt.request
        response = await client.chat(
            messages=evaled_prompt.data,
            **new_request
            ).acall()
        base_path = Path(run_config.output_path).parent.resolve() if run_config.output_path else None
        if stream:
            if run_config.output_fd:
                # stream response to a file descriptor
                run_config.output_fd.write(cls._dumps_frontmatter(new_request, run_config))
                role, content, tool_calls = await converter.astream_msgs2raw(astream_chat_all(response), run_config.output_fd)
            elif run_config.output_path:
                # stream response to a file
                with open(run_config.output_path, 'w', encoding='utf-8') as fout:
                    fout.write(cls._dumps_frontmatter(new_request, run_config, base_path))
                    role, content, tool_calls = await converter.astream_msgs2raw(astream_chat_all(response), fout)
            else:
                role, content, tool_calls = await converter.astream_msgs2raw(astream_chat_all(response))
        else:
            role = response['choices'][0]['message']['role']
            content = response['choices'][0]['message'].get('content')
            tool_calls = response['choices'][0]['message'].get('tool_calls')
        return ChatPrompt(
            [{"role": role, "content": content, "tool_calls": tool_calls}],
            new_request, run_config, base_path,
            response=response
        )

    def __add__(self, other: Union[str, list, ChatPrompt]):
        # support concatenation with string, list or another ChatPrompt
        if isinstance(other, str):
            return ChatPrompt(
                self.messages + [{"role": "user", "content": other}],
                copy.deepcopy(self.request),
                replace(self.run_config),
                self.base_path
            )
        elif isinstance(other, list):
            return ChatPrompt(
                self.messages + other,
                copy.deepcopy(self.request),
                replace(self.run_config),
                self.base_path
            )
        elif isinstance(other, ChatPrompt):
            # merge two ChatPrompt objects
            merged_request, merged_run_config = self._merge_non_data(other)
            return ChatPrompt(
                self.messages + other.messages, merged_request, merged_run_config, 
                self.base_path
            )
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'ChatPrompt' and '{type(other)}'")
    
    def __iadd__(self, other: Union[str, list, ChatPrompt]):
        # support concatenation with string, list or another ChatPrompt
        if isinstance(other, str):
            self.messages.append({"role": "user", "content": other})
        elif isinstance(other, list):
            self.messages += other
        elif isinstance(other, ChatPrompt):
            # merge two ChatPrompt objects
            self.messages += other.messages
            self._merge_non_data(other, inplace=True)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'ChatPrompt' and '{type(other)}'")
        return self


class CompletionsPrompt(HandyPrompt):
    
    def __init__(
        self, prompt: str, request: dict, meta: Union[dict, RunConfig], 
        base_path: PathType = None,
        response: Optional[dict] = None,
        ):
        super().__init__(prompt, request, meta, base_path, response)
    
    @property
    def prompt(self) -> str:
        return self.data
    
    @prompt.setter
    def prompt(self, value: str):
        self.data = value
    
    def _eval_data(self, run_config: RunConfig) -> str:
        var_map = self._parse_var_map(run_config)
        new_prompt = self.prompt
        for key, value in var_map.items():
            new_prompt = new_prompt.replace(key, value)
        return new_prompt
    
    @staticmethod
    def _stream_completions_proc(response, fd: Optional[io.IOBase] = None) -> str:
        # stream response to fd
        content = ""
        for text in stream_completions(response):
            if fd:
                fd.write(text)
            content += text
        return content

    @classmethod
    def _run_with_client(
        cls, 
        client: OpenAIClient, 
        evaled_prompt: PromptType,
        stream: bool,
        ) -> CompletionsPrompt:
        run_config = evaled_prompt.run_config
        new_request = evaled_prompt.request
        response = client.completions(
            prompt=evaled_prompt.data,
            **new_request
            ).call()
        base_path = Path(run_config.output_path).parent.resolve() if run_config.output_path else None
        if stream:
            if run_config.output_fd:
                # stream response to a file descriptor
                run_config.output_fd.write(cls._dumps_frontmatter(new_request, run_config))
                content = cls._stream_completions_proc(response, run_config.output_fd)
            elif run_config.output_path:
                # stream response to a file
                with open(run_config.output_path, 'w', encoding='utf-8') as fout:
                    fout.write(cls._dumps_frontmatter(new_request, run_config, base_path))
                    content = cls._stream_completions_proc(response, fout)
            else:
                content = cls._stream_completions_proc(response)
        else:
            content = response['choices'][0]['text']
        return CompletionsPrompt(
            content, new_request, run_config, base_path, response=response
            )

    @staticmethod
    async def _astream_completions_proc(response, fd: Optional[io.IOBase] = None) -> str:
        # stream response to fd
        content = ""
        async for text in astream_completions(response):
            if fd:
                fd.write(text)
            content += text
        return content
    
    @classmethod
    async def _arun_with_client(
        cls, 
        client: OpenAIClient, 
        evaled_prompt: PromptType,
        stream: bool,
        ) -> CompletionsPrompt:
        run_config = evaled_prompt.run_config
        new_request = evaled_prompt.request
        response = await client.completions(
            prompt=evaled_prompt.data,
            **new_request
            ).acall()
        base_path = Path(run_config.output_path).parent.resolve() if run_config.output_path else None
        if stream:
            if run_config.output_fd:
                # stream response to a file descriptor
                run_config.output_fd.write(cls._dumps_frontmatter(new_request, run_config))
                content = await cls._astream_completions_proc(response, run_config.output_fd)
            elif run_config.output_path:
                # stream response to a file
                with open(run_config.output_path, 'w', encoding='utf-8') as fout:
                    fout.write(cls._dumps_frontmatter(new_request, run_config, base_path))
                    content = await cls._astream_completions_proc(response, fout)
            else:
                content = await cls._astream_completions_proc(response)
        else:
            content = response['choices'][0]['text']
        return CompletionsPrompt(
            content, new_request, run_config, base_path, response=response
            )
    
    def __add__(self, other: Union[str, CompletionsPrompt]):
        # support concatenation with string or another CompletionsPrompt
        if isinstance(other, str):
            return CompletionsPrompt(
                self.prompt + other,
                copy.deepcopy(self.request),
                replace(self.run_config),
                self.base_path
            )
        elif isinstance(other, CompletionsPrompt):
            # merge two CompletionsPrompt objects
            merged_request, merged_run_config = self._merge_non_data(other)
            return CompletionsPrompt(
                self.prompt + other.prompt, merged_request, merged_run_config,
                self.base_path
            )
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'CompletionsPrompt' and '{type(other)}'")
    
    def __iadd__(self, other: Union[str, CompletionsPrompt]):
        # support concatenation with string or another CompletionsPrompt
        if isinstance(other, str):
            self.prompt += other
        elif isinstance(other, CompletionsPrompt):
            # merge two CompletionsPrompt objects
            self.prompt += other.prompt
            self._merge_non_data(other, inplace=True)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'CompletionsPrompt' and '{type(other)}'")
        return self

