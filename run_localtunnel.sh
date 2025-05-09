#!/bin/bash
echo "[LocalTunnel] Starting tunnel on port 8000..."
npx localtunnel --port 8000 --subdomain quasar-dev --print-requests
