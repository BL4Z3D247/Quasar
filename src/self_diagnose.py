import os

def self_diagnose():
    paths = [
        ".quasar_version",
        "src/memory.py",
        "src/supabase_logger.py",
        "src/observe.py",
        "src/version_utils.py",
        "install/",
        "archive/",
        "dataset/"
    ]
    issues = []
    for path in paths:
        full = os.path.expanduser(f"~/projects/auto-dev/{path}")
        if not os.path.exists(full):
            issues.append(f"❌ Missing: {path}")
    if not issues:
        print("✅ All critical Quasar components are present.")
    else:
        for issue in issues:
            print(issue)
