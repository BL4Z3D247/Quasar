#!/usr/bin/env bash
cd ~/projects/auto-dev
echo "[Scope Runner] PWD=$(pwd)"
echo "[Scope Runner] Invoking scope.py…"
exec python3 -u src/modules/scope.py
