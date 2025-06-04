import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def correct_english_text(user_input):
    prompt = f"""
You are an English tutor. Correct the following sentence, explain the mistake briefly, and suggest an improved version. Keep it short.

User: "{user_input}"
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a kind and helpful English conversation tutor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()