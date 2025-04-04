import unittest
from markdown_extract import extract_markdown_images

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![image1](https://example.com/img1.png) and ![image2](https://example.com/img2.png)"
        matches = extract_markdown_images(text)
        expected = [("image1", "https://example.com/img1.png"), ("image2", "https://example.com/img2.png")]
        self.assertListEqual(matches, expected)

if __name__ == "__main__":
    unittest.main()
