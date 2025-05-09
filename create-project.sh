#!/usr/bin/env bash
set -euo pipefail

# Create a new project folder, initialize git, and push to GitHub

ENV_FILE=".env"
if [[ -f "$ENV_FILE" ]]; then
  export $(grep -v '^#' "$ENV_FILE" | xargs)
fi

# ↓ NEW: your GitHub username for all SSH URLs
GITHUB_OWNER="bl4z3d247"
export GITHUB_OWNER

project_name="$1"
template_dir="templates/default"
project_path="projects/$project_name"

echo "[+] Creating GitHub repo: $project_name"
gh repo create "$GITHUB_OWNER/$project_name" --private --confirm || true

echo "[+] Cloning locally..."
git clone "git@github.com:${GITHUB_OWNER}/${project_name}.git" "$project_path"
cd "$project_path"
git checkout -b main

echo "[+] Adding template..."
cp -r "../../$template_dir/." .

echo "[+] Committing and pushing..."
git add .
git commit -m "Initial commit from automation"
git push -u origin main

echo "[✓] Project $project_name created and initialized."
