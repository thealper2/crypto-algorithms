import unittest
from morse_code import MorseCodeCipher


class TestMorseCodeCipher(unittest.TestCase):
    """
    Test cases for the MorseCodeCipher class.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of MorseCodeCipher.
        """
        self.cipher = MorseCodeCipher()

    def test_encode_valid_text(self):
        """
        Test encoding valid text into Morse code.
        """
        # Test encoding a simple text
        self.assertEqual(
            self.cipher.encode("HELLO WORLD"),
            ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
        )
        # Test encoding a text with numbers
        self.assertEqual(self.cipher.encode("123"), ".---- ..--- ...--")
        # Test encoding a text with special characters
        self.assertEqual(
            self.cipher.encode("HELLO, WORLD"),
            ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -..",
        )

    def test_encode_invalid_text(self):
        """
        Test encoding text with invalid characters.
        """
        # Test encoding text with an invalid character
        self.assertIsNone(
            self.cipher.encode("HELLO_WORLD")
        )  # '_' is not in the Morse code dictionary

    def test_decode_valid_morse_code(self):
        """
        Test decoding valid Morse code into text.
        """
        # Test decoding a simple Morse code
        self.assertEqual(
            self.cipher.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
            "HELLO WORLD",
        )
        # Test decoding Morse code with numbers
        self.assertEqual(self.cipher.decode(".---- ..--- ...--"), "123")
        # Test decoding Morse code with special characters
        self.assertEqual(
            self.cipher.decode(".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.."),
            "HELLO, WORLD",
        )

    def test_decode_invalid_morse_code(self):
        """
        Test decoding invalid Morse code.
        """
        # Test decoding Morse code with an invalid sequence
        self.assertIsNone(
            self.cipher.decode("......")
        )  # '......' is not in the reverse Morse code dictionary

    def test_encode_decode_consistency(self):
        """
        Test that encoding and decoding are consistent (i.e., encode -> decode returns the original text).
        """
        original_text = "HELLO WORLD"
        encoded_text = self.cipher.encode(original_text)
        decoded_text = self.cipher.decode(encoded_text)
        self.assertEqual(decoded_text, original_text)


if __name__ == "__main__":
    unittest.main()
