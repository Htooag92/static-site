from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    # Handle empty block early
    if not block:
        return BlockType.PARAGRAPH

    # Check if it's a heading (1-6 # characters followed by a space)
    if block.startswith("#") and block.lstrip("#").startswith(" "):
        return BlockType.HEADING

    # Check if it's a code block (starts and ends with three backticks)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Check if it's a quote block (every line starts with '>')
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Check if it's an unordered list block (every line starts with '- ')
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Check if it's an ordered list block
    lines = block.splitlines()
    if all((line.split(". ")[0]).isdigit() and i == int(line.split(". ")[0]) for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
