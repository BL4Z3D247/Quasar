import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(prompt: str, model="gpt-3.5-turbo", temperature=0.7, max_tokens=500):
    try:
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"OpenAI error: {e}"
