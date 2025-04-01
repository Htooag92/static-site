from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Append node as-is if it's not of type TEXT
            new_nodes.append(node)
        else:
            # Split the node's text
            split_text = node.text.split(delimiter)

            # Ensure delimiters are balanced
            if len(split_text) % 2 == 0:
                raise ValueError("Unmatched delimiter in text: " + repr(node.text))

            # Alternate between TEXT and the provided text_type
            for i, part in enumerate(split_text):
                if i % 2 == 0:
                    # Even index = plain text
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    # Odd index = specified text type (e.g., CODE, BOLD)
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes



