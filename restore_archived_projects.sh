#!/bin/bash

ARCHIVE_DIR="$HOME/projects/auto-dev/archived"
PROJECT_DIR="$HOME/projects/auto-dev/projects"

echo "== Archived Projects Restore Tool =="
echo

if [ ! -d "$ARCHIVE_DIR" ]; then
  echo "❌ No archived directory found at: $ARCHIVE_DIR"
  exit 1
fi

found_any=false

for project_path in "$ARCHIVE_DIR"/*; do
  project=$(basename "$project_path")
  if [ -d "$project_path" ]; then
    found_any=true
    echo "Restore project: $project? [y/N]"
    read -r answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
      if [ -d "$PROJECT_DIR/$project" ]; then
        echo "⚠️  Skipped: $project already exists in projects/"
      else
        mv -v "$project_path" "$PROJECT_DIR/"
        echo "✅ Restored: $project"
      fi
    else
      echo "⏩ Skipped: $project"
    fi
    echo
  fi
done

if [ "$found_any" = false ]; then
  echo "📦 No archived projects found in $ARCHIVE_DIR"
fi

echo "✅ Restore process complete."
