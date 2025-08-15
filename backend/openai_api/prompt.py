from typing import List, Optional
from openai_api.chat import get_gpt_response

class PromptAPI:
    def __init__(self, system_prompt: Optional[str] = None):
        self.system_prompt = system_prompt or "You are a helpful assistant."

    async def prompt(self, context: List[str]):
        """
        send a prompt to OpenAI API, injecting a system prompt 
        """
        messages = []
        prompt = self.system_prompt
        if prompt:
            messages.append({"role": "system", "content": prompt})
        for c in context:
            messages.append({"role": "user", "content": c})
        
        response = await get_gpt_response(messages)
        return response
