import subprocess

def run():
    print("[SyncRepo] Triggering Scope (git push)...")
    subprocess.run(["python3", "scope.py"], cwd="~/projects/auto-dev", shell=True)

    print("[SyncRepo] Triggering Lodestone (git pull)...")
    subprocess.run(["python3", "quasar.py", "run", "lodestone_sync"], cwd="~/projects/auto-dev", shell=True)

    print("✅ Repo sync completed.")
