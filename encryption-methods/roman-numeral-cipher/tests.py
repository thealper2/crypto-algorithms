import unittest
from roman_numeral import RomanNumeralCipher


class TestRomanNumeralCipher(unittest.TestCase):
    """
    A test class for the RomanNumeralCipher class.
    This class tests the encoding, decoding, and error handling functionalities.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of RomanNumeralCipher.
        """
        self.cipher = RomanNumeralCipher()

    def test_encode_valid_input(self):
        """
        Test encoding with valid input.
        """
        # Test encoding a simple word
        self.assertEqual(self.cipher.encode("HELLO"), "VIII V XII XII XV")
        # Test encoding a single letter
        self.assertEqual(self.cipher.encode("A"), "I")
        # Test encoding a word with mixed case (should be case-insensitive)
        self.assertEqual(self.cipher.encode("HeLlO"), "VIII V XII XII XV")

    def test_encode_invalid_input(self):
        """
        Test encoding with invalid input (non-alphabetic characters).
        """
        # Test encoding with numbers
        with self.assertRaises(ValueError):
            self.cipher.encode("HELLO123")
        # Test encoding with special characters
        with self.assertRaises(ValueError):
            self.cipher.encode("HELLO!")

    def test_decode_valid_input(self):
        """
        Test decoding with valid input.
        """
        # Test decoding a simple encoded string
        self.assertEqual(self.cipher.decode("VIII V XII XII XV"), "HELLO")
        # Test decoding a single Roman numeral
        self.assertEqual(self.cipher.decode("I"), "A")
        # Test decoding with extra spaces (should be handled gracefully)
        self.assertEqual(self.cipher.decode("  VIII   V  XII  XII  XV  "), "HELLO")

    def test_decode_invalid_input(self):
        """
        Test decoding with invalid input (invalid Roman numerals).
        """
        # Test decoding with an invalid Roman numeral
        with self.assertRaises(ValueError):
            self.cipher.decode("VIII V XII XII INVALID")
        # Test decoding with an empty string
        with self.assertRaises(ValueError):
            self.cipher.decode("")

    def test_encode_decode_round_trip(self):
        """
        Test encoding and then decoding to ensure the original text is recovered.
        """
        original_text = "HELLO"
        encoded_text = self.cipher.encode(original_text)
        decoded_text = self.cipher.decode(encoded_text)
        self.assertEqual(decoded_text, original_text)

        original_text = "PYTHON"
        encoded_text = self.cipher.encode(original_text)
        decoded_text = self.cipher.decode(encoded_text)
        self.assertEqual(decoded_text, original_text)

    def test_edge_cases(self):
        """
        Test edge cases such as empty input or single-character input.
        """
        # Test encoding an empty string
        with self.assertRaises(ValueError):
            self.cipher.encode("")
        # Test decoding an empty string
        with self.assertRaises(ValueError):
            self.cipher.decode("")
        # Test encoding a single character
        self.assertEqual(self.cipher.encode("Z"), "XXVI")
        # Test decoding a single Roman numeral
        self.assertEqual(self.cipher.decode("XXVI"), "Z")


if __name__ == "__main__":
    unittest.main()
