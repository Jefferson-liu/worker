#This agent will manage the overall functionality of the system, coordinating between different agents and handling requests.
from typing import List
from models.agent import Agent
from openai_api.prompt import PromptAPI
class Manager(Agent):
    name: str = "Manager"
    description: str = "This agent manages the overall functionality of the system, coordinating between different agents and handling requests."

    def action(self, request: str, agent_list: List[Agent]) -> str:
        """
        :param input_data: Input data for the agent to process.
        :return: Result of the action as a string.
        """
        
        return "Manager action executed with request: {}, chose to use agent ...".format(request)