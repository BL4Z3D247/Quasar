import re
from typing import Optional

def extract_command(message: str) -> Optional[str]:
    # Look for `command` patterns
    match = re.search(r"`([^`]+)`", message)
    if match:
        return match.group(1).strip()

    # Look for "Run: <command>" pattern
    if "Run:" in message:
        return message.split("Run:", 1)[-1].strip()

    # Fallback basic command pattern
    match = re.search(r"\b(ls|pwd|echo|cat|cd|mkdir|rm|touch)[^.;]*", message)
    if match:
        return match.group(0).strip()

    return None
