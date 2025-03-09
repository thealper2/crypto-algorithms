import unittest
from hexadecimal_cipher import HexadecimalCipher


class TestHexadecimalCipher(unittest.TestCase):
    """
    A test class for the HexadecimalCipher class.
    This class tests the encoding and decoding functionalities, as well as error handling.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of HexadecimalCipher.
        """
        self.cipher = HexadecimalCipher()

    def test_encode_valid_input(self):
        """
        Test encoding with valid input strings.
        """
        # Test encoding a simple string
        self.assertEqual(self.cipher.encode("Hello"), "48656c6c6f")
        # Test encoding a string with spaces
        self.assertEqual(self.cipher.encode("Hello World"), "48656c6c6f20576f726c64")
        # Test encoding a string with special characters
        self.assertEqual(self.cipher.encode("Python@123"), "507974686f6e40313233")

    def test_decode_valid_input(self):
        """
        Test decoding with valid hexadecimal strings.
        """
        # Test decoding a simple hexadecimal string
        self.assertEqual(self.cipher.decode("48656c6c6f"), "Hello")
        # Test decoding a hexadecimal string with spaces
        self.assertEqual(self.cipher.decode("48656c6c6f20576f726c64"), "Hello World")
        # Test decoding a hexadecimal string with special characters
        self.assertEqual(self.cipher.decode("507974686f6e40313233"), "Python@123")

    def test_encode_invalid_input(self):
        """
        Test encoding with invalid input (non-string types).
        """
        with self.assertRaises(ValueError):
            self.cipher.encode(123)  # Integer input
        with self.assertRaises(ValueError):
            self.cipher.encode(None)  # None input
        with self.assertRaises(ValueError):
            self.cipher.encode([1, 2, 3])  # List input

    def test_decode_invalid_input(self):
        """
        Test decoding with invalid input (non-string types or invalid hexadecimal strings).
        """
        # Test decoding with non-string input
        with self.assertRaises(ValueError):
            self.cipher.decode(123)  # Integer input
        with self.assertRaises(ValueError):
            self.cipher.decode(None)  # None input
        with self.assertRaises(ValueError):
            self.cipher.decode([1, 2, 3])  # List input

        # Test decoding with invalid hexadecimal string length
        with self.assertRaises(ValueError):
            self.cipher.decode("48656c6c6f21")  # Odd-length hexadecimal string

        # Test decoding with invalid hexadecimal characters
        with self.assertRaises(ValueError):
            self.cipher.decode("48656c6c6g")  # Invalid character 'g'

    def test_encode_decode_round_trip(self):
        """
        Test encoding and decoding round-trip to ensure consistency.
        """
        original_text = "Hello World! 123 @Python"
        encoded_text = self.cipher.encode(original_text)
        decoded_text = self.cipher.decode(encoded_text)
        self.assertEqual(original_text, decoded_text)


if __name__ == "__main__":
    unittest.main()
