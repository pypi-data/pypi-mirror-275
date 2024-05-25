import logging

from message import Message, ToolMessage
from models.base import Model
from tools.base import Tool, ToolCall


# Logger
logger = logging.getLogger(__file__)


class OpenAIModel(Model):
    _client: "OpenAI"  # type: ignore

    def _create_client(self, **client_kwargs) -> "OpenAI":  # type: ignore
        from openai import OpenAI
        return OpenAI(**client_kwargs)
    
    def convert_completion_to_messages(self,
        content: str | None,
        tool_calls: list["ChatCompletionMessageToolCall"],  # type: ignore
        tools: dict[str, Tool],
    ) -> list[Message | ToolMessage]:
        final_messages: list[Message | ToolMessage] = []

        # Create messages
        tc_for_msgs: list[ToolCall] = []
        for tc in tool_calls:
            if tc.function.name not in tools:
                logger.warning(
                    f"{tc.function.name} not found in agent's tools! Available tools are {', '.join(list(tools.keys()))}."
                )
            else:
                tc_for_msgs.append(ToolCall.from_openai_tool_call(tools[tc.function.name], tc))

        # Create a message that contains the completion's content
        message = Message(
            role="assistant",
            content=content if content else "",
            tool_calls=tc_for_msgs,
        )
        final_messages.append(message)

        # If the completion had tool calls, we need to create tool messages for each
        # tool call.
        for tc in tc_for_msgs:
            tool_msg = ToolMessage(
                tool_call_id=tc.tool_call_id,
                name=tc.tool_name,
                content=tc.output,
            )
            final_messages.append(tool_msg)

        return final_messages

    def call_completions_api(self,
        temperature: int,
        tools: list[Tool],
        conversation: list[Message | ToolMessage],
    ):
        # Call the Completions API
        completion = self._client.chat.completions.create(
              model=self._model,
              temperature=temperature,
              tools=[
                 v.derive_json_specification() for _, v in tools.items()
              ] if tools else None,
              messages=[
                c.msg for c in conversation
              ],
        )
        content = completion.choices[0].message.content
        tool_calls = completion.choices[0].message.tool_calls

        # Convert completion to a list of messages
        completion_messages = self.convert_completion_to_messages(
            content,
            [] if tool_calls is None else tool_calls,
            tools
        )

        # Return messages from this completion
        return completion_messages

    def chat(self,
        user_input: str | None,
        temperature: int,
        tools: list[Tool],
        conversation: list[Message | ToolMessage],
    ) -> list[Message | ToolMessage]:
        user_message: Message | None = (
            Message(
                role="user",
                content=user_input
            )
            if user_input
            else None
        )
        if user_message:
            conversation.append(user_message)
        return self.call_completions_api(temperature, tools, conversation)

    def chat_from_message(self,
        message: Message,
        temperature: int,
        tools: list[Tool],
        conversation: list[Message | ToolMessage],
    ) -> list[Message | ToolMessage]:
        conversation.append(message)
        return self.call_completions_api(temperature, tools, conversation)
