#This agent will create other agents and determine their roles based on the user's request.
from typing import List
from models.agent import Agent
from openai_api.prompt import PromptAPI
class AgentFactory(Agent):
    name: str = "AgentFactory"
    description: str = "This agent creates other agents and determines their roles based on the user's request."
    agent_prompt: str = """
        You are an agent factory that takes a request and generates a list of agents that will be needed to fulfill the request.
        Respond with a list of agents in the format 'AgentName | AgentDescription | AgentPrompt', one per line.
        You should consider the following when creating agents:
        - The specific tasks that need to be accomplished based on the user request.
        - The skills and expertise required for each task.
        - The roles that each agent will play in the overall system.

        Ensure that the agents are distinct and have clear responsibilities.
        Each agent should have a unique name and a clear description of its role.

        If the scope of the request is too broad or complex, you may create specialized agent factories with narrower requests for each factory. 
        Agent Factory system prompts should be the same as this one.
        The user request is:
        """

    def action(self, user_request: str) -> List[Agent]:
        """
        :param input_data: Input data for the agent to process.
        :return: Result of the action as a string.
        """
        agent = PromptAPI(system_prompt=self.agent_prompt)
        
        response = agent.prompt([user_request])
        # Parse the response to create Agent instances
        agents = []
        for line in response.split("\n"):
            if line.strip():
                try:
                    name, description, system_prompt = line.split("|", 2)
                    agents.append(Agent(name=name.strip(), description=description.strip(), system_prompt=system_prompt.strip()))
                except ValueError:
                    continue
        return agents