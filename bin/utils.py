import re


def check_kebab_case(s: str) -> bool:
    """Check if a string is in kebab-case format."""
    return bool(re.match(r"^[a-z][a-z0-9-]*[a-z0-9]$", s))
