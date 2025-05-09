import os
import subprocess

def run():
    os.chdir(os.path.expanduser("~/projects/auto-dev"))

    print("🧹 Cleaning up nested Git repos...")
    subrepos = [
        "archived/hello-world-demo-final",
        "archived/hello-world-demo",
        "archived/hello-world-demo2",
        "archived/scout-bot",
        "archived/scout-v6",
        "archived/scout-v8",
        "archived/scout-v9",
        "projects/scout-v3"
    ]

    for repo in subrepos:
        subprocess.call(["git", "rm", "--cached", repo], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("✅ Submodules removed. Staging files...")
    subprocess.call(["git", "add", "."], stdout=subprocess.DEVNULL)
    subprocess.call(["git", "commit", "-m", "Initial commit from Quasar"], stdout=subprocess.DEVNULL)

    print("🔐 Verifying GitHub SSH login...")
    subprocess.call(["gh", "auth", "login", "--hostname", "github.com", "--git-protocol", "ssh"])

    print("🚀 Creating and pushing GitHub repo via SSH...")
    subprocess.call(["gh", "repo", "create", "Quasar", "--public", "--source=.", "--remote=origin", "--push"])

    print("✅ Quasar has deployed itself to GitHub.")
