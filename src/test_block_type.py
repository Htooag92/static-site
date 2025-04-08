import unittest
from block_type import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_valid_heading(self):
        # Valid headings
        self.assertEqual(block_to_block_type("# Heading Level 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading Level 4"), BlockType.HEADING)

    def test_invalid_heading_no_space(self):
        # Invalid: no space after ##
        self.assertEqual(block_to_block_type("##Heading Level 2"), BlockType.PARAGRAPH)
        # Invalid: empty block
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)

    def test_not_a_heading(self):
        # Plain text shouldn't be a heading
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        # Improperly formatted heading
        self.assertEqual(block_to_block_type("   #####Invalid"), BlockType.PARAGRAPH)

    def test_valid_code_block(self):
        # Single-line code block
        self.assertEqual(block_to_block_type("```\nprint('Hello, World!')\n```"), BlockType.CODE)

        # Empty code block
        self.assertEqual(block_to_block_type("```\n\n```"), BlockType.CODE)

        # Multi-line code block
        self.assertEqual(
            block_to_block_type("```\ndef hello():\n    print('Hello, World!')\n```"),
            BlockType.CODE
        )  # Ensures multi-line code block is recognized

    def test_valid_quote(self):
        # Single-line quote
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

        # Multi-line quote
        self.assertEqual(
            block_to_block_type("> Line 1\n> Line 2\n> Line 3"), BlockType.QUOTE)

        # Invalid quote (not all lines start with >)
        self.assertEqual(
            block_to_block_type("> Line 1\nLine 2\n> Line 3"), BlockType.PARAGRAPH)

    def test_valid_unordered_list(self):
        # Single-line unordered list
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDERED_LIST)

        # Multi-line unordered list
        self.assertEqual(
            block_to_block_type("- Item 1\n- Item 2\n- Item 3"), BlockType.UNORDERED_LIST
        )

        # Invalid unordered list (only some lines start with '- ')
        self.assertEqual(
            block_to_block_type("- Valid item\nInvalid line"), BlockType.PARAGRAPH
        )
        
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        block = "1. First\n3. Skipped\n4. Still here"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        block = "1 First\n2 Second\n3 Third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
