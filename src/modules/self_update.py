import subprocess

def run():
    print("[Quasar] Updating to latest version from GitHub...")
    subprocess.run(["python3", "quasar.py", "run", "lodestone_sync"])

    print("[Quasar] Regenerating documentation...")
    subprocess.run(["python3", "quasar.py", "run", "build_readme"])
    subprocess.run(["python3", "quasar.py", "run", "build_landing_page"])
    subprocess.run(["python3", "quasar.py", "run", "build_logo_brief"])

    print("[Quasar] Logging update commit to memory...")
    subprocess.run(["python3", "quasar.py", "run", "log_commit"])

    print("✅ Quasar has updated itself and refreshed documentation.")
