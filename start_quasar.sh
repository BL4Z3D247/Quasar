#!/bin/bash
export $(grep -v '^#' ~/projects/auto-dev/.env | xargs)

# Restart Flask bot
pm2 restart quasar-telegram --update-env

# Kill any old ngrok processes
pkill ngrok || true

# Start ngrok in the background
nohup ngrok http 8443 --log=stdout > ~/ngrok.log 2>&1 &

# Wait for ngrok to initialize
sleep 6

# Get new public ngrok URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -oE "https://[a-z0-9.-]+\.ngrok(-free)?\.app")

# Register Telegram webhook
curl -F "url=${NGROK_URL}/${TELEGRAM_BOT_TOKEN}" https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setWebhook

echo "✅ Quasar is live at: $NGROK_URL"
