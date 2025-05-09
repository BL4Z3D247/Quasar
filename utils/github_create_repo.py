# utils/github_create_repo.py

import os
import sys
import requests

GITHUB_USERNAME = "BL4Z3D247"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def create_repo(repo_name):
    if not GITHUB_TOKEN:
        print("ERROR: GITHUB_TOKEN environment variable not set.")
        return

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    data = {
        "name": repo_name,
        "private": False,
        "auto_init": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"[✓] GitHub repository '{repo_name}' created successfully.")
    else:
        print(f"[✗] Failed to create GitHub repo: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 utils/github_create_repo.py <repo_name>")
        sys.exit(1)

    create_repo(sys.argv[1])
