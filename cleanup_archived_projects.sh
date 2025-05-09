#!/bin/bash
echo "== Cleanup Archived Projects =="
read -p "Delete all projects in ~/projects/auto-dev/archived? [y/N] " confirm
if [[ "$confirm" =~ ^[Yy]$ ]]; then
  rm -rf ~/projects/auto-dev/archived/*
  echo "✅ Archived projects deleted."
else
  echo "⏹ Cancelled. No changes made."
fi
