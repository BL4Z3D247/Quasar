import os
from datetime import datetime
from src.model_wrapper import chat_with_retry

AUTOGEN_DIR = os.path.expanduser("~/projects/auto-dev/autogen")

def generate_code(task_description: str) -> str:
    prompt = f"""Write a complete, minimal Python 3 script to accomplish the following task:
\"\"\"{task_description}\"\"\"
Make sure it's well-formatted and works without any external input or configuration."""

    messages = [{"role": "user", "content": prompt}]
    response = chat_with_retry(messages)

    # Extract code from triple backticks
    lines = response.split("\n")
    code_lines = []
    inside_code = False
    for line in lines:
        if "```" in line:
            inside_code = not inside_code
            continue
        if inside_code:
            code_lines.append(line)

    final_code = "\n".join(code_lines).strip()
    return final_code

def save_code(code: str, filename: str = None) -> str:
    if not os.path.exists(AUTOGEN_DIR):
        os.makedirs(AUTOGEN_DIR)

    if not filename:
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"autogen_{timestamp}.py"

    filepath = os.path.join(AUTOGEN_DIR, filename)
    with open(filepath, "w") as f:
        f.write(code)

    return filepath
