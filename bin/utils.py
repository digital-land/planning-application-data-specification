import os
import re


def check_kebab_case(s: str) -> bool:
    """Check if a string is in kebab-case format."""
    return bool(re.match(r"^[a-z][a-z0-9-]*[a-z0-9]$", s))


def save_string_to_file(content: str, file_path: str):
    """
    Save a string to a file, ensuring the folder exists.
    """
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
