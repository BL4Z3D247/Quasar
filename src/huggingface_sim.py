# src/huggingface_sim.py

def simulate_response(prompt: str) -> str:
    """Case-insensitive fallback for exec, math, etc."""
    text = prompt.strip()
    low = text.lower()

    # Exec commands: return with 'Run:' prefix
    if low.startswith("run:"):
        # find the colon in original to preserve case and spacing
        idx = text.lower().find("run:")
        cmd = text[idx + len("run:"):].strip()
        return f"Run: {cmd}"

    # Common file ops
    if "list files" in low or low.startswith("ls"):
        return "Run: ls -la"
    if "status" in low or low.startswith("uptime"):
        return "Run: uptime"

    # Math fallback
    if any(op in low for op in ["+", "-", "*", "/"]):
        return f"Run: echo $(({low}))"

    # Default fallback
    return f"[Hugging Face] Simulated response to: '{prompt}'"
