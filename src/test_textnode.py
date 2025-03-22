import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_no_url(self):
        node = TextNode("Sample text", TextType.TEXT)
        node2 = TextNode("Sample text", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()


