#This agent will manage the overall functionality of the system, coordinating between different agents and handling requests.
from typing import List
from models.agent import Agent
from openai_api.prompt import PromptAPI
class Manager(Agent):
    name: str = "Manager"
    description: str = "This agent recieves a list of agents and decides the best suited one based on their descriptions."

    def action(self, request: str, agent_list: List[Agent]) -> str:
        """
        :param input_data: Input data for the agent to process.
        :return: Result of the action as a string.
        """
        agent_dict = {agent.name: agent for agent in agent_list}
        manager = PromptAPI(system_prompt=self.description)
        prompt = "You are a manager that decides on what the best agent to use for this task: {} " \
        "given a list of agent names and descriptions. Here is a list of agents and their descriptions: {}. " \
        "Respond only with the name of the best agent to use." \
        "The best agent to use is:".format(request, ", ".join([f"{agent.name}: {agent.description}" for agent in agent_list]))
        response = manager.prompt([prompt])
        return agent_dict[response].action(request)
        