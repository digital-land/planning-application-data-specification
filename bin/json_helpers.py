import json
import os
from typing import Any, Dict


def save_json(data: Dict[str, Any], filename: str = "cache/github_issues_cache.json"):
    """Save issues to JSON file with fetch timestamp."""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved data issues to {filename}")
    return filename


def load_json(
    filename: str = "cache/github_issues_cache.json",
) -> tuple[Dict[str, Any]]:
    """Load issues from JSON file and return issues + timestamp."""
    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

    # Handle old format (just a list) vs new format (dict with metadata)
    if isinstance(data, list):
        issues = data
        timestamp = "Unknown (old format)"
    else:
        issues = data.get("issues", [])
        timestamp = data.get("fetch_timestamp_human", "Unknown")

    print(f"Loaded {len(issues)} issues from {filename} (last fetched: {timestamp})")
