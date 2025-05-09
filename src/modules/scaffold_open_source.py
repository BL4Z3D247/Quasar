import os

def run():
    base = os.path.expanduser("~/projects/auto-dev")

    print("📁 Creating standard open-source structure...")
    folders = [
        "docs", "examples", "tests", "scripts", ".github/workflows"
    ]
    for folder in folders:
        os.makedirs(os.path.join(base, folder), exist_ok=True)

    print("✅ Folder structure in place.")

    print("📝 Generating metadata and documentation files...")
    with open(os.path.join(base, "CONTRIBUTING.md"), "w") as f:
        f.write("# Contributing to Quasar\n\nThanks for helping evolve the first autonomous developer.")

    with open(os.path.join(base, "LICENSE"), "w") as f:
        f.write("MIT License\n\nPermission is hereby granted, free of charge...")

    with open(os.path.join(base, ".github", "workflows", "ci.yml"), "w") as f:
        f.write("""name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python3 -m unittest discover -s tests
""")

    with open(os.path.join(base, "requirements.txt"), "w") as f:
        f.write("openai\ngitpython\npydantic")

    print("✅ Metadata, license, CI, and requirements generated.")
    print("🧠 Quasar is now structured like a full open-source developer project.")
