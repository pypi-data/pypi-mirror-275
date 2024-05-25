from typing import Any, Callable
import json
import uuid

from tools.base import Tool


class ToolCall:

    def __init__(self,
        tool: Tool,
        tool_name: str,
        tool_arguments: dict[str, Any]
    ):
        self.tool_call_id = self.set_tool_call_id()
        self.tool = tool
        self.tool_name = tool_name
        self.tool_arguments = tool_arguments
        self._output = self.tool.func(**self.tool_arguments)
    
    def set_tool_call_id(self):
        return str(uuid.uuid4())

    @classmethod
    def from_openai_tool_call(cls,
        tool: Tool,
        completion_tool_call: "ChatCompletionMessageToolCall"  # type: ignore
    ):
        tool_arguments = json.loads(completion_tool_call.function.arguments)
        tool_name = completion_tool_call.function.name
        return cls(
            tool=tool,
            tool_name=tool_name,
            tool_arguments=tool_arguments
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