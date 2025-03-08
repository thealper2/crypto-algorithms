import unittest
from base_85 import Base85Cipher


class TestBase85(unittest.TestCase):
    """
    Unit tests for the Base85 encoding and decoding implementation.
    """

    def setUp(self):
        """
        Set up the Base85 instance for testing.
        """
        self.base85 = Base85Cipher()

    def test_encode_basic(self):
        """
        Test basic encoding functionality.
        """
        # Test encoding a simple string
        data = "Hello"
        encoded = self.base85.encode(data)
        self.assertEqual(encoded, "87cURDZ")

    def test_decode_basic(self):
        """
        Test basic decoding functionality.
        """
        # Test decoding a simple Base85 string
        encoded = "87cURDZ"
        decoded = self.base85.decode(encoded)
        self.assertEqual(decoded, "Hello")

    def test_encode_decode_roundtrip(self):
        """
        Test encoding and decoding roundtrip to ensure data integrity.
        """
        data = "Hello, World!"
        encoded = self.base85.encode(data)
        decoded = self.base85.decode(encoded)
        self.assertEqual(decoded, data)

    def test_encode_zero_bytes(self):
        """
        Test encoding of zero bytes (special case for 'z').
        """
        data = b"\x00\x00\x00\x00"
        encoded = self.base85.encode(data)
        self.assertEqual(encoded, "z")

    def test_decode_zero_bytes(self):
        """
        Test decoding of the special 'z' character.
        """
        encoded = "z"
        decoded = self.base85.decode(encoded)
        self.assertEqual(decoded, b"\x00\x00\x00\x00")

    def test_encode_padding(self):
        """
        Test encoding with padding (input length not a multiple of 4).
        """
        data = "Hi"
        encoded = self.base85.encode(data)
        self.assertEqual(encoded, "5SB")

    def test_decode_padding(self):
        """
        Test decoding with padding (input length not a multiple of 5).
        """
        encoded = "5SB"
        decoded = self.base85.decode(encoded)
        self.assertEqual(decoded, "Hi")

    def test_encode_invalid_input(self):
        """
        Test encoding with invalid input (non-bytes type).
        """
        with self.assertRaises(TypeError):
            self.base85.encode("Invalid input")

    def test_decode_invalid_input(self):
        """
        Test decoding with invalid input (non-string type).
        """
        with self.assertRaises(TypeError):
            self.base85.decode(b"Invalid input")

    def test_decode_invalid_character(self):
        """
        Test decoding with an invalid Base85 character.
        """
        encoded = "87cURD*"  # '*' is not a valid Base85 character
        with self.assertRaises(ValueError):
            self.base85.decode(encoded)

    def test_decode_invalid_length(self):
        """
        Test decoding with an invalid Base85 string length.
        """
        encoded = "87cUR"  # Length is not a multiple of 5 and not padded
        with self.assertRaises(ValueError):
            self.base85.decode(encoded)


if __name__ == "__main__":
    unittest.main()
