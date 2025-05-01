#!/bin/bash
cd /home/deploy/projects/auto-dev

# log startup
echo "[DEBUG] $(date): Scope watcher STARTED" >> logs/scout.log

# watch for changes
while inotifywait -r -e modify,create,delete src .env; do
  echo "[DEBUG] $(date): Change detected" >> logs/scout.log
  git add .
  git commit -m "Auto-update from Scope @ $(date +'%Y-%m-%d %H:%M:%S')" || true
  git push origin main || true
done
