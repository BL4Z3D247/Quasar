#!/bin/bash

ARCHIVE_DIR="$HOME/projects/auto-dev/archived"
PROJECT_DIR="$HOME/projects/auto-dev/projects"

IGNORE_LIST=(
  "scope-test"
  "smoke-test"
  "hello-world-demo"
  "hello-world-demo-final"
  "hello-world-demo2"
  "scout-v6"
  "scout-v8"
  "scout-v9"
  "scout-bot"
)

mkdir -p "$ARCHIVE_DIR"

echo "Archiving ignored projects..."
for project in "${IGNORE_LIST[@]}"; do
  if [ -d "$PROJECT_DIR/$project" ]; then
    mv -v "$PROJECT_DIR/$project" "$ARCHIVE_DIR/"
  else
    echo "[skip] $project not found, skipping."
  fi
done

echo "✅ Archiving complete."
