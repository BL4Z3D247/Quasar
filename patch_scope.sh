#!/bin/bash

cd ~/projects/auto-dev || exit 1

# Step 1: Inject IGNORE list after WATCH_DIR
sed -i '/WATCH_DIR =/a IGNORE = {"scope-test","smoke-test","scout-alpha-test","hello-world-demo","hello-world-demo-final","hello-world-demo2","scout-v6","scout-v8","scout-v9","scout-bot"}' src/modules/scope.py

# Step 2: Patch os.walk loop
sed -i '/for root, dirs, _ in os.walk(WATCH_DIR):/a \
    name = os.path.basename(root)\n\
    if name in IGNORE or ".git" not in dirs:\n\
        continue' src/modules/scope.py

# Step 3: Stop and delete any old scope-watcher process
pm2 delete scope-watcher || true

# Step 4: Start or restart 'scope' process
pm2 delete scope || true
pm2 start src/modules/scope.py --name scope --interpreter python3 --cwd ~/projects/auto-dev -f --update-env

# Step 5: Persist PM2 state and flush logs
pm2 save
pm2 flush scope

# Done
echo -e "\n✅ scope fully patched and restarted clean. Logs:"
pm2 logs scope --lines 5
