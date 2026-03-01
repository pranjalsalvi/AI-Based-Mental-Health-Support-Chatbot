# gemini_client.py
import os
from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()  # Load .env file automatically

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Check your .env file.")
        self.client = Groq(api_key=api_key)  # API key now loaded from env

    def generate_response(self, prompt: str, history=None) -> dict:
        """
        Returns a structured response dictionary with natural, short responses.
        """
        try:
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a compassionate and supportive mental health assistant. "
                        "Always respond naturally, in four separate short sentences or lines: "
                        "1) Empathy, 2) Prompt/Question, 3) Suggestion, 4) Encouragement. "
                        "Do NOT include headings like 'Empathy Statement' or 'Practical Suggestion'. "
                        "Keep each part short and human-like."
                    )
                }
            ]

            # Include previous conversation
            if history:
                for item in history:
                    messages.append({"role": "user", "content": item.get("user", "")})
                    messages.append({"role": "assistant", "content": item.get("assistant", "")})

            messages.append({"role": "user", "content": prompt})

            # Call Groq API
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model="llama-3.1-8b-instant",  # make sure this model is active
                temperature=0.7,
                max_tokens=500,
            )

            raw_response = chat_completion.choices[0].message.content.strip()

            # Split response into sentences (more natural than \n\n)
            sentences = re.split(r'(?<=[.!?])\s+', raw_response)

            # Map sentences to structured response
            response = {
                "empathy": sentences[0] if len(sentences) > 0 else "",
                "prompt": sentences[1] if len(sentences) > 1 else "",
                "suggestion": sentences[2] if len(sentences) > 2 else "",
                "encouragement": sentences[3] if len(sentences) > 3 else ""
            }

            return response

        except Exception as e:
            return {
                "empathy": f"I'm here to listen. {str(e)}",
                "prompt": "",
                "suggestion": "",
                "encouragement": ""
            }