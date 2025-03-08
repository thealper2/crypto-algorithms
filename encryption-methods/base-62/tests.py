import unittest
from base_62 import Base62Cipher


class TestBase62Cipher(unittest.TestCase):
    """
    Test cases for the Base62Cipher class.
    """

    def setUp(self):
        """Initialize the Base62Cipher instance for testing."""
        self.cipher = Base62Cipher()

    def test_encode_positive_integer(self):
        """Test encoding of positive integers."""
        self.assertEqual(self.cipher.encode(0), "0")  # Edge case: smallest input
        self.assertEqual(self.cipher.encode(12345), "3d7")  # Regular case
        self.assertEqual(self.cipher.encode(999999), "4c91")  # Larger number

    def test_encode_invalid_input(self):
        """Test encoding with invalid inputs (non-integer or negative values)."""
        with self.assertRaises(ValueError):
            self.cipher.encode(-1)  # Negative integer
        with self.assertRaises(ValueError):
            self.cipher.encode("123")  # String input
        with self.assertRaises(ValueError):
            self.cipher.encode(12.34)  # Float input

    def test_decode_valid_string(self):
        """Test decoding of valid Base62 strings."""
        self.assertEqual(self.cipher.decode("0"), 0)  # Edge case: smallest input
        self.assertEqual(self.cipher.decode("3d7"), 12345)  # Regular case
        self.assertEqual(self.cipher.decode("4c91"), 999999)  # Larger number

    def test_decode_invalid_string(self):
        """Test decoding with invalid Base62 strings."""
        with self.assertRaises(ValueError):
            self.cipher.decode("")  # Empty string
        with self.assertRaises(ValueError):
            self.cipher.decode("3d7@")  # Invalid character
        with self.assertRaises(ValueError):
            self.cipher.decode(12345)  # Non-string input

    def test_encode_decode_consistency(self):
        """Test that encoding and decoding are consistent (round-trip)."""
        test_numbers = [0, 1, 123, 999999, 987654321]
        for number in test_numbers:
            encoded = self.cipher.encode(number)
            decoded = self.cipher.decode(encoded)
            self.assertEqual(decoded, number, f"Round-trip failed for {number}")


if __name__ == "__main__":
    unittest.main()
