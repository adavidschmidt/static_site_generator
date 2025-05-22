import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_different_type(self):
		node3 = TextNode("This is a link node", TextType.LINK)
		node4 = TextNode("This is an link node", TextType.IMAGE)
		self.assertNotEqual(node3, node4)

	def test_different_text(self):
		node5 = TextNode("This is a bold node", TextType.BOLD)
		node6 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node5, node6)

	def test_with_url(self):
		node7 = TextNode("This is text", TextType.TEXT, "test.url")
		node8 = TextNode("This is text", TextType.TEXT, "test.url")
		self.assertEqual(node7, node8)

	def test_with_different_url(self):
		node9 = TextNode("This is text", TextType.TEXT, "test.com")
		node10 = TextNode("This is text", TextType.TEXT, "test.url")
		self.assertNotEqual(node9, node10)

	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
  
	def test_bold(self):
		node = TextNode("This is a text node", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
	unittest.main()
