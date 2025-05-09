from src.exec_engine import run_command

print(run_command("echo Test run in safe mode"))
print(run_command("rm -rf /tmp/fakefolder", safe_mode=True))
