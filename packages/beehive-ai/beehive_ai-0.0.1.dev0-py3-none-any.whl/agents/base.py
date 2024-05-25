import logging
import os
from rich.logging import RichHandler
from typing import Any, Callable

from models.base import Model
from tools.base import Tool
from message import Message, ToolMessage


# Logging
logging.basicConfig(
    level="WARN",
    format="%(message)s",
    handlers=[
        RichHandler()
    ],
)
logger = logging.getLogger(__file__)


class Invokable:
    name: str
    _description: str
    _conversation: list[Message | ToolMessage]

    def __init__(self, name: str, description: str):
        self.name = name
        self._description = description
        self._conversation = []
    
    def invoke(self, task: str | None = None) -> list[Message | ToolMessage]:
        raise NotImplementedError()
    
    def stream(self, task: str | None = None) -> list[Message | ToolMessage]:
        raise NotImplementedError()

    def invoke_from_message(self, message: Message | None = None) -> list[Message | ToolMessage]:
        raise NotImplementedError()


class PrismAgent(Invokable):
    name: str
    _description: str
    _model: Model
    _temperature: int
    _tools: dict[str, Tool]

    _system_message: Message
    _conversation: list[Message | ToolMessage]
    _conversation_fpath: os.PathLike | None


    def __init__(self,
        name: str,
        model: Model,
        temperature: int = 0,
        description: str = "You are a helpful assistant.",
        tools: list[Callable[..., Any]] | None = None,
        conversation_fpath: os.PathLike | None = None,
    ):
        
        super().__init__(name, description)
        self._model = model
        self._client = self._model._client
        self._temperature = temperature        
        if tools:
            self._tools = {
                x.__name__: Tool(x) for x in tools
            }
        else:
            self._tools: dict[str, Tool] = {}

        self._conversation_fpath = conversation_fpath

        self.setup()
    
    def setup(self):
        self.set_system_message(self._description)
    
    def set_system_message(self, system_message: str):
        self._system_message = Message(
            role="system",
            content=system_message,
        )
        self._set_initial_conversation()

    def __str__(self):
        classname = self.__class__.__name__
        return f"{classname}(name='{self.name}', model={self._model}, tools=[{', '.join(list(self._tools.keys()))}])"

    def _set_initial_conversation(self):
        self._conversation: list[Message] = [self._system_message]

    @property
    def system_message(self):
        return self._system_message

    @system_message.setter
    def system_message(self, new_system_prompt: str):
        self._system_message = Message(
            role="system",
            content=new_system_prompt
        )
        self._set_initial_conversation()

    @property
    def conversation(self) -> list[Message]:
        return self._conversation

    @conversation.setter
    def conversation(self, _):
        raise ValueError("`conversation` property is read-only!")
    
    def reset_conversation(self):
        logger.warning((
            "Resetting the conversation means your agent will lose all of the messages in its memory."
            " Use this with caution."
        ))
        self._set_initial_conversation()

    def invoke(self, task: str | None = None) -> list[Message | ToolMessage]:
        messages = self._model.chat(
            task,
            self._temperature,
            self._tools,
            self._conversation,
        )

        # Add these messages to the agent's conversation. That way, if a user invokes
        # the agent sequentially, the agent can build off of previous results.
        self._conversation.extend(messages)
        return messages

    def invoke_from_message(self, message: Message) -> list[Message | ToolMessage]:
        messages = self._model.chat_from_message(
            message,
            self._temperature,
            self._tools,
            self._conversation,
        )

        # Add these messages to the agent's conversation. That way, if a user invokes
        # the agent sequentially, the agent can build off of previous results.
        self._conversation.extend(messages)
        return messages
