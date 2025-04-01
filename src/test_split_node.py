from textnode import TextNode, TextType
from split_node import split_nodes_delimiter

# Test case 1: Simple delimiter splitting
node1 = TextNode("This is `code` in a sentence.", TextType.TEXT)
delimiter = "`"
text_type = TextType.CODE

new_nodes = split_nodes_delimiter([node1], delimiter, text_type)
for node in new_nodes:
    print(f"Text: {node.text}, Type: {node.text_type}")

# Test case 2: Unmatched delimiters
try:
    node2 = TextNode("This is `unmatched delimiter test.", TextType.TEXT)
    split_nodes_delimiter([node2], delimiter, text_type)
except ValueError as e:
    print(e)

# Test case 3: Multiple occurrences of the delimiter
node3 = TextNode("`Code1` and `Code2` appear here.", TextType.TEXT)
new_nodes = split_nodes_delimiter([node3], delimiter, text_type)
for node in new_nodes:
    print(f"Text: {node.text}, Type: {node.text_type}")

# Test case 4: No delimiter present
node4 = TextNode("This is just plain text.", TextType.TEXT)
new_nodes = split_nodes_delimiter([node4], delimiter, text_type)
for node in new_nodes:
    print(f"Text: {node.text}, Type: {node.text_type}")
