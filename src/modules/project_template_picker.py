from src.module_loader import run_module

def run():
    print("[Template] Ask user: 'What kind of project? (e.g., react, cli, flask, api)'")
    # Placeholder, could be made dynamic later
    choice = "react"
    run_module(f"scaffold_{choice}")
