import os
from src.model_wrapper import call_openai

def call_model(prompt):
    try:
        return call_openai(prompt)
    except Exception as e:
        return f"⚠️ Failed to call OpenAI: {e}"
