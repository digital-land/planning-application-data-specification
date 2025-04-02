import re


def slugify(text):
    """Convert a string into a URL-friendly slug"""
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'[\s/]+', '-', text)
    # Remove all characters that are not alphanumeric or hyphens
    text = re.sub(r'[^\w\-]', '', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text
