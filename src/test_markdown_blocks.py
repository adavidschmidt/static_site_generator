import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

class TextMarkdwonToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_block_to_block_type_code(self):
        block = """```\nsome text goes here\n```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_normal(self):
        block = """This is a normal paragraph"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
    def test_block_to_block_type_heading(self):
        block = """### This is a heading"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_block_to_block_type_unordered(self):
        block = """- This is an unorder list\n- Item 2"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
        
    def test_block_to_block_type_quote(self):
        block = """> This is a quote\n> still a quote"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
        
    def test_block_to_block_type_ordered(self):
        block = """1. This is a orderd list\n2. second"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)