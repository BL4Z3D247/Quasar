import importlib
import os

def list_modules():
    path = os.path.expanduser("~/projects/auto-dev/src/modules")
    return [f.replace(".py", "") for f in os.listdir(path) if f.endswith(".py")]

def run_module(module_name):
    try:
        mod = importlib.import_module(f"src.modules.{module_name}")
        if hasattr(mod, "run"):
            mod.run()
        else:
            print(f"❌ Module '{module_name}' found, but has no 'run()' function.")
    except ModuleNotFoundError:
        print(f"❌ Module '{module_name}' not found.")

def run_agent_sequence(task_string):
    from time import sleep
    tasks = [t.strip() for t in task_string.split(",") if t.strip()]
    print(f"⚙️  Agent starting sequence: {tasks}")
    for task in tasks:
        print(f"\n▶ Running: {task}")
        run_module(task)
        sleep(1)
