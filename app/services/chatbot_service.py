from app.api.gemini_client import GeminiClient
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.memory.session_memory import get_chat_history

class ChatbotService:

    def __init__(self):
        self.client = GeminiClient()

    def get_response(self, user_input):

        history = get_chat_history()

        structured_prompt = f"""
        {SYSTEM_PROMPT}

        Conversation History:
        {history}

        User: {user_input}
        """

        response = self.client.generate_response(structured_prompt, history)

        return response