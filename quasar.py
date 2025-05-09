import os

def get_identity():
    try:
        with open(os.path.expanduser("~/projects/auto-dev/.quasar_name")) as f:
            return f.read().strip()
    except:
        return "Quasar"

import os
#!/usr/bin/env python3
import sys
import os
from src.model_router import call_model
from src.exec_engine import run_command
from src.intent_parser import extract_command
from src.memory import recall

# Import your new modules
from src.modules.scope import watch_changes, on_change
from src.modules.lodestone import pull_changes
from src.modules.scribble import show_logs

def review_memory(n=5):
    entries = recall(n)
    if not entries:
        print("📖 No memory entries found.")
        return
    print(f"📖 Reviewing last {len(entries)} tasks:")
    for i, e in enumerate(entries, 1):
        print(f"\n--- Entry {i} ---")
        print(f"Time: {e['timestamp']}")
        print(f"Prompt: {e['prompt']}")
        if e.get("command"):
            print(f"Command: {e['command']}")
            print(f"Output: {e['output']}")
        else:
            print(f"Response: {e['response']}")

def improve_memory(n=5):
    entries = recall(n)
    if not entries:
        print("🔧 Nothing to improve—no memory found.")
        return
    summary = "\n".join(
        f"{i+1}. Prompt: {e['prompt']} | Response: {e.get('response','')} | Command: {e.get('command','')}"
        for i, e in enumerate(entries)
    )
    review_prompt = (
        "You are Quasar, an AI assistant that improves its own performance. "
        f"Here are my last {len(entries)} tasks:\n{summary}\n"
        "For each task, suggest one way I could have done it better or more efficiently."
    )
    suggestion = call_model([{"role": "user", "content": review_prompt}])
    print("\n🛠️ Improvement Suggestions:\n")
    print(suggestion)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  quasar.py \"Your prompt here\"")
        print("  quasar.py review [N]")
        print("  quasar.py improve [N]")
        print("  quasar.py watch")
        print("  quasar.py pull <repo-path>")
        print("  quasar.py logs [N]")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "review":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        review_memory(n)
        sys.exit(0)

    if cmd == "improve":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        improve_memory(n)
        sys.exit(0)

    if cmd == "watch":
        print("🔍 Starting scope watcher…")
        watch_changes(on_change)
        sys.exit(0)

    if cmd == "pull":
        path = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
        pull_changes(path)
        sys.exit(0)

    if cmd == "observe":
        content = sys.argv[2] if len(sys.argv) > 2 else None
        if not content:
            print("Usage: quasar.py observe \"your message\" [--tag optional]")
            sys.exit(1)
        tag = None
        if "--tag" in sys.argv:
            tag_index = sys.argv.index("--tag") + 1
            if tag_index < len(sys.argv):
                tag = sys.argv[tag_index]
        from src.observe import observe
        observe(content=content, role="user", tag=tag)
        sys.exit(0)

    if cmd == "self-diagnose":
        from src.self_diagnose import self_diagnose
        self_diagnose()
        sys.exit(0)

    if cmd == "generate":
        if len(sys.argv) < 3:
            print("Usage: quasar.py generate \"command_name: code\"")
            sys.exit(1)
        from src.generate import generate
        raw = sys.argv[2]
        if ":" in raw:
            name, code = raw.split(":", 1)
            generate(name.strip(), code.strip())
        else:
            print("❌ Please format as: name: code")
        sys.exit(0)

    if cmd == "run":
        if len(sys.argv) < 3:
            print("Usage: quasar.py run <module_name>")
            sys.exit(1)
        from src.module_loader import run_module
        run_module(sys.argv[2])
        sys.exit(0)

    if cmd == "agent":
        if len(sys.argv) < 3:
            print("Usage: quasar.py agent \"mod1,mod2,...\"")
            sys.exit(1)
        from src.module_loader import run_agent_sequence
        run_agent_sequence(sys.argv[2])
        sys.exit(0)

    if cmd == "schedule":
        if len(sys.argv) < 4:
            print("Usage: quasar.py schedule <module> <HH:MM>")
            sys.exit(1)
        from src.scheduler import add_schedule
        add_schedule(sys.argv[2], sys.argv[3])
        sys.exit(0)

    if cmd == "run-schedule":
        from src.scheduler import run_due_tasks
        run_due_tasks()
        sys.exit(0)

    if cmd == "queue":
        if len(sys.argv) < 3:
            print("Usage: quasar.py queue <module>")
            sys.exit(1)
        import json, os
        qfile = os.path.expanduser("~/projects/auto-dev/.quasar_queue.json")
        queue = json.load(open(qfile)) if os.path.exists(qfile) else []
        queue.append(sys.argv[2])
        json.dump(queue, open(qfile, "w"), indent=2)
        print(f"✅ Queued: {sys.argv[2]}")
        sys.exit(0)

    if cmd == "daemon":
        from src.daemon import daemon_loop
        daemon_loop()
        sys.exit(0)

    if cmd == "observe-passive":
        from src.modules.self_observer import run
        run()
        sys.exit(0)

    if cmd == "list-commands":
        print(f"\n=== Available Commands for {get_identity()} ===")
        print("observe       → Log an idea or message")
        print("logs [N]      → Show last N execution logs")
        print("review [N]    → Review last N memory entries")
        print("improve [N]   → Suggest improvements from memory")
        print("list-commands → Display this help menu")
        print("===================================")
        sys.exit(0)

    if cmd == "logs":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        show_logs(n)
        sys.exit(0)

    # Regular AI prompt
    prompt = sys.argv[1]
    messages = [{"role": "user", "content": prompt}]
    response = call_model(messages)
    print(f"[Quasar CLI] You said: {prompt}")
    print(response)

    # Execute if command found
    cmd_to_run = extract_command(response)
    if cmd_to_run:
        output = run_command(cmd_to_run)
        print(output)

if __name__ == "__main__":
    main()
