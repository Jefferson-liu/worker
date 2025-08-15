from typing import List, Optional

class PromptAPI:
    def __init__(self, default_system_prompt: Optional[str] = None):
        self.default_system_prompt = default_system_prompt or "You are a helpful assistant."

    def build_messages(self, user_messages: List[dict], system_prompt: Optional[str] = None) -> List[dict]:
        """
        Build a list of messages for OpenAI API, injecting a system prompt if provided.
        :param user_messages: List of dicts with 'text' and 'sender' keys.
        :param system_prompt: Optional custom system prompt.
        :return: List of messages for OpenAI API.
        """
        messages = []
        prompt = system_prompt or self.default_system_prompt
        if prompt:
            messages.append({"role": "system", "content": prompt})
        for m in user_messages:
            role = "user" if m["sender"] == "user" else "assistant"
            messages.append({"role": role, "content": m["text"]})
        return messages
