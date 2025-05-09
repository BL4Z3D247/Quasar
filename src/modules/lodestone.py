import os, subprocess, logging

def pull_changes(repo_path: str):
    print(f"[Lodestone] Pulling changes in {repo_path}")
    git_dir = os.path.join(repo_path, ".git")
    if not os.path.isdir(git_dir):
        print(f"[Lodestone]   ↳ not a git repo, skipping")
        return

    # Try to pull; if no remote or fail, bail out
    try:
        subprocess.run(
            ["git", "-C", repo_path, "pull"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print(f"[Lodestone]   ↳ pull succeeded")
    except subprocess.CalledProcessError as e:
        logging.error(f"[Lodestone] git pull failed: {e}")
        print(f"[Lodestone]   ↳ pull failed, skipping restart")
        return

    service = os.path.basename(repo_path)
    # Check if PM2 knows about this service
    res = subprocess.run(
        ["pm2", "describe", service],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    if res.returncode != 0:
        print(f"[Lodestone]   ↳ PM2 service '{service}' not found, skipping restart")
        return

    # Restart the live service
    try:
        print(f"[Lodestone]   ↳ restarting PM2 service '{service}'")
        subprocess.run(["pm2", "restart", service], check=True)
        print(f"[Lodestone]   ↳ service '{service}' restarted")
    except subprocess.CalledProcessError as e:
        logging.error(f"[Lodestone] pm2 restart {service} failed: {e}")

