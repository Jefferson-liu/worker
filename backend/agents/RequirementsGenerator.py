from typing import List
from models.agent import Agent
from backend.models.prompt import PromptAPI
class RequirementsGenerator(Agent):
    name: str = "RequirementsGenerator"
    description: str = "This agent recieves user messages and generates a list of technical requirements based on the input."

    def action(self, user_request: str, clarifications: List[str]) -> str:
        """
        :param input_data: Input data for the agent to process.
        :return: Result of the action as a string.
        """
        manager = PromptAPI(system_prompt=self.description)
        prompt = "You are a requirements generator that takes user requests and generates a list of technical requirements. " \
        "Here is the user request: {}. " \
        "Here are some clarifications: {}. " \
        "Respond with a list of technical requirements based on the user request and clarifications.".format(user_request, ", ".join(clarifications))
        response = manager.prompt([prompt])
        return response
        