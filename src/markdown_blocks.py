from enum import Enum
import re


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
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("-"):
        for line in lines:
            if not line.startswith("-"):
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
    html = "<div>"
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)


def text_to_children(text):




    for block in blocks:
        block_type = block_to_block_type(block)
        for line in block:
            pass
            

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