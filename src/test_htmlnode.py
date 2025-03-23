import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with no props
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single prop
        node = HTMLNode("a", "Click me!", props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(
            "a", 
            "Click me!",
            props={
                "href": "https://www.example.com",
                "target": "_blank",
                "class": "link"
            }
        )
        # The order of props might vary, so check for each one separately
        result = node.props_to_html()
        self.assertIn(' href="https://www.example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertIn(' class="link"', result)
        
    def test_repr(self):
        # Test the __repr__ method
        node = HTMLNode("p", "Hello", props={"class": "text"})
        self.assertIn("HTMLNode", repr(node))
        self.assertIn("p", repr(node))
        self.assertIn("Hello", repr(node))
        self.assertIn("class", repr(node))

if __name__ == "__main__":
    unittest.main()
