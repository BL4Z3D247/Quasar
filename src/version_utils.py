import os
from datetime import datetime

INSTALL_DIR = os.path.expanduser("~/projects/auto-dev/install")
VERSION_FILE = os.path.expanduser("~/projects/auto-dev/.quasar_version")

def check_and_generate_installer(current_version: str):
    os.makedirs(INSTALL_DIR, exist_ok=True)
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE) as f:
            previous_version = f.read().strip()
    else:
        previous_version = None
    if current_version != previous_version:
        filename = os.path.join(INSTALL_DIR, f"quasar-{current_version}.sh")
        with open(filename, "w") as f:
            f.write(f"# Quasar Installer for {current_version}\\n")
            f.write(f"# Generated on {datetime.utcnow().isoformat()}\\n")
            f.write("# TODO: Insert tracked changes here\\n")
        with open(VERSION_FILE, "w") as f:
            f.write(current_version)
        print(f"✅ Generated new installer: {filename}")
    else:
        print(f"ℹ️ Quasar is already up to date (v{current_version})")
