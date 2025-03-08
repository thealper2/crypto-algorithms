import unittest
from base_58 import Base58Cipher


class TestBase58(unittest.TestCase):
    """
    Test suite for the Base58 encoding and decoding implementation.
    """

    def setUp(self):
        """
        Set up the Base58 instance for testing.
        """
        self.base58 = Base58Cipher()

    def test_encode_empty_input(self):
        """
        Test encoding with empty input. Should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.base58.encode(b"")

    def test_decode_empty_input(self):
        """
        Test decoding with empty input. Should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.base58.decode("")

    def test_encode_basic(self):
        """
        Test encoding a basic byte string.
        """
        input_data = b"hello"
        expected_output = "Cn8eVZg"
        self.assertEqual(self.base58.encode(input_data), expected_output)

    def test_decode_basic(self):
        """
        Test decoding a basic Base58 string.
        """
        input_data = "Cn8eVZg"
        expected_output = b"hello"
        self.assertEqual(self.base58.decode(input_data), expected_output)

    def test_encode_with_leading_zeros(self):
        """
        Test encoding a byte string with leading zeros.
        """
        input_data = b"\x00\x00hello"
        expected_output = "11Cn8eVZg"
        self.assertEqual(self.base58.encode(input_data), expected_output)

    def test_decode_with_leading_ones(self):
        """
        Test decoding a Base58 string with leading '1's (which represent leading zeros in bytes).
        """
        input_data = "11Cn8eVZg"
        expected_output = b"\x00\x00hello"
        self.assertEqual(self.base58.decode(input_data), expected_output)

    def test_encode_decode_roundtrip(self):
        """
        Test encoding and decoding roundtrip to ensure consistency.
        """
        input_data = b"Base58 encoding is fun!"
        encoded = self.base58.encode(input_data)
        decoded = self.base58.decode(encoded)
        self.assertEqual(decoded, input_data)

    def test_decode_invalid_characters(self):
        """
        Test decoding a Base58 string with invalid characters. Should raise a ValueError.
        """
        invalid_input = "Cn8eVZg0OIl"  # Contains invalid characters '0', 'O', 'I', 'l'
        with self.assertRaises(ValueError):
            self.base58.decode(invalid_input)

    def test_encode_large_data(self):
        """
        Test encoding a large byte string.
        """
        input_data = b"x" * 1000  # 1000 bytes of 'x'
        encoded = self.base58.encode(input_data)
        decoded = self.base58.decode(encoded)
        self.assertEqual(decoded, input_data)

    def test_decode_large_data(self):
        """
        Test decoding a large Base58 string.
        """
        input_data = "1" * 1000  # 1000 '1's (representing 1000 leading zeros)
        decoded = self.base58.decode(input_data)
        self.assertEqual(decoded, b"\x00" * 1000)


if __name__ == "__main__":
    unittest.main()
