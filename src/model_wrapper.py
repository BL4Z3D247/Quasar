import os
import time
import openai
from dotenv import load_dotenv
from src.huggingface_sim import simulate_response
from src.memory import remember

# Load .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

openai.api_key = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

def call_openai(messages):
    resp = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0.7
    )
    return resp.choices[0].message.content

def call_huggingface(messages):
    return simulate_response(messages[-1]["content"])

def chat_with_retry(messages, max_attempts=3):
    prompt_text = messages[-1]["content"]
    for attempt in range(1, max_attempts + 1):
        print(f"[Quasar] OpenAI attempt {attempt}/{max_attempts}")
        try:
            content = call_openai(messages)
            remember(prompt=prompt_text, response=content)
            return content
        except Exception as e:
            print(f"[OpenAI Error] {e}")
            time.sleep(1)
    # Fallback
    print("[Model Response] Falling back to Hugging Face simulation.")
    content = call_huggingface(messages)
    remember(prompt=prompt_text, response=content)
    return content
