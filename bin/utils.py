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


# New helpers for name/anchor formatting
def to_anchor(s: str) -> str:
    """
    Convert a string into a URL-safe kebab-case anchor.
    e.g. "Site constraint" -> "site-constraint"
    """
    if not s:
        return ""
    s = s.lower()
    # replace any sequence of non-alphanumeric characters with a single hyphen
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s


# func to take string, split on separator and return list
def split_string(s: str, separator: str = ";") -> list:
    """
    Split a string by a separator (default ';') and return a list of trimmed substrings.
    """
    if not s:
        return []
    return [part.strip() for part in s.split(separator) if part.strip()]


def split_field_in_dicts(
    dicts: list, key: str, separator: str = ";", in_place: bool = True
) -> list:
    """
    For each dict in `dicts`, if `key` exists and its value is a string,
    replace that value with the result of `split_string(value, separator)`.

    Parameters
    - dicts: list of dictionaries to process
    - key: the key to look for in each dictionary
    - separator: separator passed to `split_string` (default ';')
    - in_place: if True mutate the dicts in place and return them; if False
      return a new list with copies of the dicts modified.

    Returns the processed list of dictionaries.
    """
    if not isinstance(dicts, list):
        raise TypeError("dicts must be a list of dictionaries")

    target_list = dicts if in_place else [d.copy() for d in dicts]

    for d in target_list:
        if not isinstance(d, dict):
            # skip non-dictionary items
            continue
        if key in d:
            val = d.get(key)
            if isinstance(val, str):
                d[key] = split_string(val, separator)

    return target_list


def make_hyperlink_cell(name: str, url: str) -> str:
    """
    Create a Google Sheets HYPERLINK formula string.

    Args:
        name (str): The text to display in the cell.
        url (str): The URL to link to.

    Returns:
        str: A string that can be written into a Google Sheet cell.
    """
    return f'=HYPERLINK("{url}", "{name}")'
