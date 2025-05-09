import subprocess

def run():
    print("[Lodestone] Pulling latest changes from GitHub...")
    try:
        subprocess.run(["git", "pull"], cwd="~/projects/auto-dev", shell=True, check=True)
        print("✅ Lodestone pulled latest repo changes.")
    except subprocess.CalledProcessError:
        print("❌ Failed to pull from GitHub.")
