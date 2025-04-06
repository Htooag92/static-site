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

def extract_markdown_links(text):
    """
    Extracts all links from the given markdown text.

    Args:
        text (str): The raw Markdown string to extract links from.

    Returns:
        list: A list of tuples where each tuple contains the link text and URL.
    """
    pattern = r"\[([^\[\]]*)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_link(old_nodes):
    """
    Split TextNodes based on markdown link syntax.
    
    Args:
        old_nodes (list): List of TextNode objects
        
    Returns:
        list: New list of TextNode objects with links extracted
    """
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        
        remaining_text = old_node.text
        for link_text, url in links:
            link_markdown = f"[{link_text}]({url})"
            sections = remaining_text.split(link_markdown, 1)
            
            if sections[0]:  # Add text before the link
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            
            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""
        
        if remaining_text:  # Add any remaining text
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes
