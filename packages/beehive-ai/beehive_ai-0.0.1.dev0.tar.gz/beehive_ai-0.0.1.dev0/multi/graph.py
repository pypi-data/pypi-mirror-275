from enum import Enum
from collections import defaultdict
import json
from typing import Literal, Tuple

from agents.base import Invokable, PrismAgent
from message import Message, ToolMessage
from models.openai_model import OpenAIModel

from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain.output_parsers import PydanticOutputParser


import logging
logger = logging.getLogger(__file__)


class EnsembleNode:
    _agent: Invokable
    _next: list[Invokable]

    def __init__(self,
        agent: Invokable,
        routes: list[Tuple[Invokable, Invokable]],
    ):
        self._agent = agent

        # Define the set of nodes that this node can talk to. We determine this by
        # parsing the `routes`.
        self._next: list[Invokable] = []
        for x in routes:
            
            # If the source is not the current agent, ignore. This should never happen.
            if x[0].name != self._agent.name:
                continue

            # Otherwise, append the target to to `_next`
            self._next.append(x[1])
    
    @property
    def name(self):
        return self._agent.name

    @property
    def description(self):
        return self._agent._description


class EnsembleWorkflow(Invokable):
    name: str
    _description: str
    _invokables: list[Invokable]
    _agent_map: dict[str, Invokable]
    _routes: list[Tuple[Invokable, Invokable]]
    _entrypoint: Invokable
    _router: Invokable | None
    state: list[Message | ToolMessage]

    _nodes: dict[str, EnsembleNode]
    _entrypoint_node: EnsembleNode

    def __init__(self,
        name: str,
        description: str,
        agents: list[Invokable],
        routes: list[Tuple[Invokable, Invokable]],
        entrypoint: Invokable,
        router: PrismAgent | None
    ):
        super().__init__(name, description)
        self._invokables = agents
        self._invokable_map = {x.name: x for x in self._invokables}
        self._routes = routes
        self._entrypoint = entrypoint

        # Router agent. This is an LLM that is used to route the workflow to the next
        # agent. This is only used if the current agent can speak with multiple
        # different agents.
        self._router = router

        # Nodes
        self._nodes = self._parse_routes()
        self._entrypoint_node = EnsembleNode(entrypoint, routes)

        # Initialize a state. This is a list of messages, and it's used to keep track of
        # the conversation. States are what allow agents to speak with one another.
        self.state: list[Message | ToolMessage] = []

    def _parse_routes(self) -> dict[str, EnsembleNode]:
        # To avoid iterating through the full list of routes for every single agent,
        # start by splitting the routes by their source node.
        source_to_routes: dict[Invokable, list[Tuple[Invokable, Invokable]]] = defaultdict(list)
        for x in self._routes:
            source_to_routes[x[0]].append(x)
        node_map = {k.name: EnsembleNode(k, v) for k, v in source_to_routes.items()}
        
        # Next, add any agents without any routes
        for x in self._invokables:
            if x.name not in node_map:
                node_map[x.name] = EnsembleNode(x, [])
        return node_map
    
    def create_enum_class_for_next_agent(self, node_next: list[Invokable]) -> "NextAgent":
        NextAgent = Enum("NextAgent", [x.name for x in node_next])
        return NextAgent

    def prompt_router_for_next_agent(self, node: EnsembleNode) -> Message:

        # Format instructions using a Pydantic parser
        valid_agent_names: list[str] = [x.name for x in node._next]
        valid_agent_names.append("FINISH")
        class NextAgentActor(BaseModel):
            agent: Literal[tuple(valid_agent_names)] = Field(description="The next agent to act. 'FINISH' if the user's original question has been answered.")  # type: ignore
            reason: str = Field(description="Rationale for choosing the next agent.")

            # @validator("agent")
            # def valid_agent(cls, field):
            #     if field not in valid_agent_names:
            #         raise ValueError(f"Invalid agent `{field}`!")
        pydantic_parser = PydanticOutputParser(pydantic_object=NextAgentActor)
        format_instructions = pydantic_parser.get_format_instructions()

        # Construct and return message
        valid_agent_descriptions = "\n".join([
            f"{x.name}: {x._description}" for x in node._next
        ])
        message = Message(
            role="system",
            content=(
                "You are a routing agent in charge of directing a conversation between"
                " agents. Each agent is an LLM model. Given the conversation above,"
                " who should act next? Choose one of the following:"
                "\n{valid_agent_descriptions}\n"
                " Please give your reasoning for your selection."
                " {format_instructions}"
            ).format(
                valid_agent_descriptions=valid_agent_descriptions,
                format_instructions=format_instructions,
            )
        )
        return message

    def invoke(self,
        task: str,
        recursion_limit: int = 100,
    ):
        task_message = Message(
            role="user",
            content=task
        )
        self.state.append(task_message)

        # Add the task message to each agent's conversation
        for inv in self._invokables:
            inv._conversation.append(task_message)
        if self._router:
            self._router._conversation.append(task_message)

        # First, direct the conversation to the entrypoint.
        previous_node: EnsembleNode | None = None
        current_node: EnsembleNode = self._entrypoint_node

        counter = 0
        completion_messages: list[Message | ToolMessage] = []
        while True:
            if counter > recursion_limit:
                break
            counter += 1

            print("-----")
            print(current_node._agent.name)

            # If the current node is different than the previous node, then extend the
            # current node's conversation using the previous iteration's completion
            # messages.
            if not previous_node or previous_node.name != current_node.name:
                current_node._agent._conversation.extend(completion_messages)

            # Invoke the current agent and overwrite the completion messages
            completion_messages = current_node._agent.invoke()
            for message in completion_messages:
                message.pprint()

            # Add messages to the state
            previous_node = current_node
            self.state.extend(completion_messages)

            # If there are no agents that need to act next, then return
            if len(current_node._next) == 0:
                break

            # Otherwise, the current node has a few potential routes that it can go
            # down. Figure out the next agent, if any, should act next.
            else:
                if not self._router:
                    raise ValueError("Need to specify a router to direct communcation between agents!")

                self._router._conversation.extend(completion_messages)

                # Prompt router
                print("----")
                print(self._router.name)
                prompt_msg = self.prompt_router_for_next_agent(current_node)
                router_messages = self._router.invoke_from_message(prompt_msg)
                next_agent_message = router_messages[-1]
                try:
                    next_agent_json = json.loads(next_agent_message.content)
                    next_agent_name = next_agent_json['agent']
                    print(f"Agent {next_agent_name} should act next. {next_agent_json['reason']}")
                except json.JSONDecodeError as e:
                    logger.error(next_agent_message.content)
                    logger.error(e)
                    continue
                except KeyError as e:
                    logger.error(str(next_agent_json))
                    logger.error(e)
                    continue

                # If we're not finished, then invoke the next agent
                if next_agent_name != "FINISH":
                    try:
                        current_node = self._nodes[next_agent_name]    
                    except KeyError:
                        print(f"Could not find agent `{next_agent_name}`!")
                else:
                    break

        return self.state
