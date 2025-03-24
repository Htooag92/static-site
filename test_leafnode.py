import unittest
from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_to_html_without_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("div", None)
            node.to_html()

# This allows the tests to run automatically when you execute this file
if __name__ == "__main__":
    unittest.main()
