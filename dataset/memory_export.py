import os
from src.memory import recall
import json

def export_memory(filename="memory_export.json", limit=100):
    data = recall(limit)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Memory exported to {filename}")
