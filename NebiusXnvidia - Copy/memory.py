import json
import os

MEMORY_FILE = "recycling_history.json"

def load_memory():
    """Loads past recycling history from your local computer."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"recycled_items": []}

def save_recycled_item(item_name):
    """Saves a newly recycled item to your local history file."""
    data = load_memory()
    data["recycled_items"].append(item_name)
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_stats():
    """Returns total items tracked so far."""
    data = load_memory()
    return len(data["recycled_items"])