import json
import logging

from agents.base import PrismAgent
from multi.prompts import (
    SupervisorPrompt,
    SupervisorNextAgentPrompt,
    SupervisorFinalAnswerPrompt,
)
from models.base import Model
from message import Message
from output import ConsoleManager


logger = logging.getLogger(__file__)


class Supervisor():
    name: str
    _agents: dict[str, PrismAgent]
    _system_prompt: str
    _supervisor_agent: PrismAgent
    _state: list[Message]
    
    def __init__(self,
        name: str,
        model: Model,
        temperature: int = 0,
        worker_agents: list[PrismAgent] | None = None,
    ):
        self._name = name
        self._agents = {x.name: x for x in worker_agents} if worker_agents else {}
        agent_names_list = list(self._agents.keys())
        if not worker_agents or len(agent_names_list) <= 1:
            raise ValueError("supervisor must manage a conversation between multiple agents!")

        # Supervisor prompt
        prompt = SupervisorPrompt.from_args(worker_agents)
        self._supervisor_agent = PrismAgent(
            name="supervisor-agent",
            model=model,
            temperature=temperature,
            description=prompt.compiled,
        )

        # Create a state. Each agent maintains their own conversations. The state
        # enables agents to share outputs and message with one another.
        self._state: list[Message] = []

    def prompt_supervisor_for_next_agent(self) -> Message:
        agent_options = ', '.join(list(self._agents.keys()))
        prompt = SupervisorNextAgentPrompt.from_args(agent_options=agent_options)
        msg = Message(
            role="system",
            content=prompt.compiled
        )
        return msg
        
    def invoke(self,
        task: str,
        recursion_limit: int = 100,
    ):
        human_message = Message(
            role="user",
            content=task
        )
        self._supervisor_agent._conversation.append(human_message)
        self._state.append(human_message)

        counter = 0
        while True:
            if counter > recursion_limit:
                break
            counter += 1

            # Invoke supervisor
            print("-----")
            next_agent_msg = self._supervisor_agent.invoke_from_message(
                self.prompt_supervisor_for_next_agent(),
            )
            self._supervisor_agent._conversation.extend(next_agent_msg)
            try:
                resp = json.loads(next_agent_msg[-1].content)
                next_agent = resp['agent']
                next_agent_rationale = resp.get('reason', "")
            except json.JSONDecodeError:
                next_agent = next_agent_msg[-1].content

            if next_agent == "FINISH":
                print(f"Supervisor: ", next_agent_rationale)
                prompt = SupervisorFinalAnswerPrompt.from_args(task=task)
                content = self._supervisor_agent.invoke(prompt.compiled)
                for x in content:
                    x.pprint()
                break
            else:
                print(f"Supervisor: ", next_agent_rationale)
                print("-----")
                print(f"{next_agent}:")
                
                # Invoke the agent that it called
                agent = self._agents[next_agent]
                # agent._conversation.extend(self._state)
                agent_completion_messages = agent.invoke()
                for x in agent_completion_messages:
                    x.pprint()

                # Add messages to supervisor agent and state
                self._supervisor_agent._conversation.extend(agent_completion_messages)
                for _, v in self._agents.items():
                    v._conversation.extend(agent_completion_messages)
                self._state.extend(agent_completion_messages)

        return None
                
    @property
    def agents(self):
        return self._agents

    @agents.setter
    def agents(self):
        raise ValueError("`agents` property is read-only!")
