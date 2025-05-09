#!/usr/bin/env bash
set -euo pipefail

# This script patches create-project.sh to include your GitHub owner and
# correct the clone/push URLs automatically.

PROJECT_DIR="$HOME/projects/auto-dev"
SCRIPT="$PROJECT_DIR/create-project.sh"
BACKUP="$PROJECT_DIR/create-project.sh.bak.$(date +%s)"

# 1) Backup existing script
echo "Backing up $SCRIPT to $BACKUP"
cp "$SCRIPT" "$BACKUP"

# 2) Fix shebang on line 1
sed -i '1s|.*|#!/usr/bin/env bash|' "$SCRIPT"

# 3) Ensure set -euo pipefail on line 2
if ! sed -n '2p' "$SCRIPT" | grep -q 'set -euo pipefail'; then
  sed -i '2i set -euo pipefail' "$SCRIPT"
fi

# 4) Insert GITHUB_OWNER after .env loader block
sed -i '/^if
