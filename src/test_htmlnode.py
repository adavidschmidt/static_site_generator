import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		node = (HTMLNode(props={"href": "https://www.google.com", "target": "_blank",}).props_to_html())
		node2 = ' href="https://www.google.com" target="_blank"'
		self.assertEqual(node, node2)

	def test_fail_props_to_html(self):
		node = (HTMLNode(props={"href": "https://www.google.com", "target": "_blank",}).props_to_html())
		node2 = ' href="https://www.boot.dev" target="_blank"'
		self.assertNotEqual(node, node2)

	def test_htmlnode_repr(self):
		node = (HTMLNode(tag="a", value="test text", children=None, props={"href": "https://www.google.com", "target": "_blank",}).__repr__())
		node2 = "tag: a, value: test text, children: None, props: {'href': 'https://www.google.com', 'target': '_blank'}"
		self.assertEqual(node, node2)

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
  
	def test_leaf_to_html_none(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")
  
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, world!")
		self.assertEqual(node.to_html(), "<a>Hello, world!</a>")
  
class testParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
	        parent_node.to_html(),
	        "<div><span><b>grandchild</b></span></div>",
	    )
        
    def test_to_html_with_greatgrandchildren(self):
        great_grandchild_node = LeafNode("p", "great grandchilde")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
	        parent_node.to_html(),
	        "<div><span><b><p>great grandchilde</p></b></span></div>",
	    )