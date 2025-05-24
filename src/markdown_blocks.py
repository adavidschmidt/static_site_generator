from enum import Enum
import re
from htmlnode import ParentNode, LeafNode, HTMLNode
from converters import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    return markdown.strip().split("\n\n")

def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)
    block_children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        text = get_block_text(block, block_type)
        
        if block_type == BlockType.CODE:
            text_node = TextNode(text, TextType.TEXT)
            block_children.append(ParentNode("pre", [ParentNode(get_block_tag(block_type),[text_node_to_html_node(text_node)])]))
            continue
        
        if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            list_children = []
            for i in text:
                children = text_to_children(i)
                list_children.append(ParentNode("li", children))
            block_children.append(ParentNode(get_block_tag(block_type), list_children))
            continue
        
        if block_type == BlockType.HEADING:
            i = len(text[0])
            children = text_to_children(text[1])
            block_children.append(ParentNode(f"{get_block_tag(block_type)}{i}", children))
            continue
        
        children = text_to_children(text)
        block_children.append(ParentNode(get_block_tag(block_type), children))
        
    return ParentNode("div", block_children)

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    nodes = []
    for node in text_nodes:
        nodes.append(text_node_to_html_node(node))
    children.extend(nodes)
    return children

def get_block_text(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            block_text = []
            for line in block.split("\n"):
                block_text.append(line)
            return " ".join(block_text)
        case BlockType.QUOTE:
            block_text = []
            for line in block:
                line_split = line.split("> ")
                block_text.appen(line_split[1])
            return " ".join(block_text)
        case BlockType.UNORDERED_LIST:
            block_text = []
            for line in block:
                line_split = line.split("- ")
                block_text.append(line_split)
            return block_text
        case BlockType.ORDERED_LIST:
            block_text = []
            for line in block:
                line_split = re.split(r"?<=\d\. ", line)
                block_text.append(line_split)
            return block_text
        case BlockType.HEADING:
            block_text = block.split(" ", 1)
            block_text = block_text[1].split("\n")
            return " ".join(block_text)
        case BlockType.CODE:
            block_text = block.split("```")
            return block_text[1].lstrip("\n")
        
def get_block_tag(block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case BlockType.CODE:
            return "code"
        case BlockType.HEADING:
            return "h"
        case _:
            raise ValueError("unrecognized block type")