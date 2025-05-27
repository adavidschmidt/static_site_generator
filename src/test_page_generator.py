import unittest
from page_generator import extract_title

class TestGenerator(unittest.TestCase):
    def test_title_exists(self):
        md = """# This is the title\nrandom text\nrandom text"""
        title = extract_title(md)
        self.assertEqual(title, "This is the title")
        
    def test_title_several_lines_down(self):
        md = """## This is the title\nrandom text\nrandom text\nradom line\n# Actual title"""
        title = extract_title(md)
        self.assertEqual(title, "Actual title")
        
    def test_title_does_not_exist(self):
        md = """## This is the title\nrandom text\nrandom text\nradom line\n### Actual title"""
        with self.assertRaises(ValueError):
            extract_title(md)