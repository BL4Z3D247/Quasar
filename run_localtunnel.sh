#!/bin/bash
echo "[LocalTunnel] Launching tunnel at subdomain quasar-dev..."
npx localtunnel --port 8000 --subdomain quasar-dev --print-requests
