from pydantic import BaseModel
from abc import ABC, abstractmethod
class Agent(BaseModel, ABC):
    name: str
    description: str
    
    @abstractmethod
    def action(self):
        """
        Perform an action based on the input data.
        This method should be overridden by subclasses to implement specific agent behavior.
        :param input_data: Input data for the agent to process.
        :return: Result of the action as a string.
        """
        raise NotImplementedError("Subclasses must implement this method.")