import re

def extract_markdown_images(text):
    """
    Extracts all images from the given markdown text.

    Args:
        text (str): The raw Markdown string to extract images from.

    Returns:
        list: A list of tuples where each tuple contains the alt text and URL.
    """
    pattern = r"!\[([^\[\]]*)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches
