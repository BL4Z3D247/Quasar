#!/bin/bash
# This script can be used in GitHub Actions or CI pipelines
echo "🚀 CI: Pulling latest from GitHub..."
git pull origin main
echo "✅ CI: Quasar has been updated."
pm2 restart quasar
