import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def correct_english_text(user_input):
    prompt = f"""Corrija e melhore o texto a seguir para um inglês natural:\n\n{user_input}"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um corretor de inglês útil e educado."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"].strip()
