from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        
        new_node = []
        if len(split_text) % 2 == 0:
            raise ValueError("incorrect markdown ensure delimiter is closed")
        for i, text in enumerate(split_text):
            if i % 2 == 0:
                new_node.append(TextNode(text, TextType.TEXT))
            else:
                new_node.append(TextNode(text, text_type))                   
        new_nodes.extend(new_node)
            
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_link(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        current_text = node.text
        new_node = []
        while current_text:
            images = extract_markdown_images(current_text)
            if images:
                alt_text, url = images[0][0], images[0][1]
                split_text = current_text.split(f"![{alt_text}]({url})", 1)
                if split_text[0]:
                    new_node.append(TextNode(split_text[0], TextType.TEXT))
                new_node.append(TextNode(alt_text, TextType.IMAGE, url))
                current_text = split_text[1]
                continue
            else:
                new_node.append(TextNode(current_text, TextType.TEXT))
                break
        new_nodes.extend(new_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        current_text = node.text
        new_node = []
        while current_text:
            links = extract_markdown_link(current_text)
            if links:
                alt_text, url = links[0][0], links[0][1]
                split_text = current_text.split(f"[{alt_text}]({url})", 1)
                if split_text[0]:
                    new_node.append(TextNode(split_text[0], TextType.TEXT))
                new_node.append(TextNode(alt_text, TextType.LINK, url))
                if len(split_text) > 1:
                    current_text = split_text[1]
                else:
                    current_text = ""
                continue
            else:
                new_node.append(TextNode(current_text, TextType.TEXT))
                break
        new_nodes.extend(new_node)
    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    new_nodes_bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    new_nodes_italic = split_nodes_delimiter(new_nodes_bold, "_", TextType.ITALIC)
    new_nodes_code = split_nodes_delimiter(new_nodes_italic, "`", TextType.CODE)
    new_nodes_images = split_nodes_image(new_nodes_code)
    new_nodes_links = split_nodes_link(new_nodes_images)
    return new_nodes_links

def markdown_to_blocks(markdown):
    return markdown.strip().split("\n\n")
    