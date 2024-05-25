from typing import Any, Callable
import json
import uuid

from .docstring import (
    get_properties_from_docstring
)


class Tool:
    
    def __init__(self,
        func: Callable[..., Any]
    ):
        self.func = func
        self.name = self.func.__name__

    def derive_json_specification(self) -> dict[str, str | dict[str, Any]]:
        spec = get_properties_from_docstring(
            function_name=self.name,
            docstring=self.func.__doc__,
        )
        return spec.serialize()


class ToolCall:

    def __init__(self,
        tool: Tool,
        tool_name: str,
        tool_arguments: dict[str, Any],
        tool_call_id: str | None = None,

    ):
        self.tool_call_id = str(uuid.uuid4()) if not tool_call_id else tool_call_id
        self.tool = tool
        self.tool_name = tool_name
        self.tool_arguments = tool_arguments
        self._output = self.tool.func(**self.tool_arguments)

    @classmethod
    def from_openai_tool_call(cls,
        tool: Tool,
        completion_tool_call: "ChatCompletionMessageToolCall"  # type: ignore
    ):
        tool_call_id = completion_tool_call.id
        tool_arguments = json.loads(completion_tool_call.function.arguments)
        tool_name = completion_tool_call.function.name
        return cls(
            tool=tool,
            tool_name=tool_name,
            tool_arguments=tool_arguments,
            tool_call_id=tool_call_id,
        )

    def serialize(self):
        function_response = {
            "name": self.tool_name,
            "arguments": json.dumps(self.tool_arguments)
        }
        return {
            "id": self.tool_call_id,
            "type": "function",
            "function": function_response
        }

    @property
    def output(self):
        return self._output