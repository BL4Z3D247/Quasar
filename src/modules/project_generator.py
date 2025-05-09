from src.model_router import call_model
from src.code_generator import generate_code_from_prompt

def run():
    print("[ProjectGen] Generating project...")
    prompt = input("Prompt: ")
    generate_code_from_prompt(prompt)
