#!/bin/bash
cd /home/deploy/projects/auto-dev
git add logs/scout.log
git commit -m "Log update @ $(date '+%Y-%m-%d %H:%M:%S')" || true
git push origin main || true
