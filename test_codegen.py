from src.code_generator import generate_code, save_code
from src.exec_engine import run_command

task = "Print the current time and date, and save it to a file named output.txt"
code = generate_code(task)
filepath = save_code(code)

print(f"✅ Code saved to: {filepath}")
print("Executing generated script in safe mode...\n")
result = run_command(f"python3 {filepath}", safe_mode=True)
print(result)
