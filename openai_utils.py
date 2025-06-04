import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def correct_english_text(user_input):
    messages = [
        {"role": "system", "content": "Você é um corretor de inglês útil e educado. Corrija e melhore o texto que eu enviar."},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"].strip()
