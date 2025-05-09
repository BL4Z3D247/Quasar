import subprocess
def run():
    print("[Deploy] Deploying to GitHub Pages...")
    subprocess.run(["git", "add", "."], cwd="~/projects/auto-dev", shell=True)
    subprocess.run(["git", "commit", "-m", "Auto-deploy"], cwd="~/projects/auto-dev", shell=True)
    subprocess.run(["git", "push"], cwd="~/projects/auto-dev", shell=True)
