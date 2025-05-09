import sys
sys.path.append("utils")

from telegram_alert import send_telegram_alert

command = sys.argv[1] if len(sys.argv) > 1 else None

if not command:
    print("No command provided.")
    exit(1)

if "build scout bot" in command.lower():
    # Trigger the automation script
    import subprocess
    subprocess.run(["bash", "create-project.sh", "scout-bot"])
    asyncio.run(send_telegram_alert("Quasar: Scout Bot build initiated."))
else:
    send_telegram_alert(f"Quasar: Command not recognized — {command}")
