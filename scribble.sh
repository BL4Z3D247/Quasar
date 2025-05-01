#!/bin/bash

# Load env vars (GIST_TOKEN, GIST_ID, etc)
set -a
source "$(dirname "$0")/.env"
set +a

cd "$(dirname "$0")"

# 1) Commit raw log (force, since it's in .gitignore)
git add -f logs/scout.log
git commit -m "Log update @ $(date '+%Y-%m-%d %H:%M:%S')" || true
git push origin main || true

# 2) Scrub & convert to JSON-lines for public Gist
jq -R -c 'split("\n")[:-1]
    | map(gsub("[1-9A-HJ-NP-Za-km-z]{32,44}"; "<REDACTED>"))
    | .[]' logs/scout.log > logs/scout-public.log

# 3) Build Gist payload and send
payload=$(jq -n --argfile file logs/scout-public.log \
  '{ files: { "scout-public.log": { content: ($file | join("\n")) } } }')

curl -s -X PATCH \
  -H "Authorization: token $GIST_TOKEN" \
  -H "Content-Type: application/json" \
  -d "$payload" \
  "https://api.github.com/gists/$GIST_ID"
