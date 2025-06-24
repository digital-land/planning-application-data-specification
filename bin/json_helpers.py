import json
import os
from typing import Any, Dict


def save_json(data: Dict[str, Any], filename: str = "cache/github_issues_cache.json"):
    """Save issues to JSON file with fetch timestamp."""

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved data issues to {filename}")
    return filename


def load_json(
    filename: str = "cache/github_issues_cache.json",
) -> tuple[Dict[str, Any]]:
    """Load issues from JSON file and return issues + timestamp."""
    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data
