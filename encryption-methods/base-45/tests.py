import unittest
from base_45 import Base45Cipher


class TestBase45(unittest.TestCase):
    """
    Test cases for the Base45 encoding and decoding functionality.
    """

    def setUp(self):
        """
        Initialize the Base45 encoder/decoder before each test.
        """
        self.base45 = Base45Cipher()

    def test_encode(self):
        """
        Test encoding functionality with valid input.
        """
        # Test encoding a simple string
        self.assertEqual(self.base45.encode("Hello"), "%69 VDL2")
        # Test encoding bytes
        self.assertEqual(self.base45.encode(b"Hello"), "%69 VDL2")
        # Test encoding an empty string (should raise an error)
        with self.assertRaises(ValueError):
            self.base45.encode("")

    def test_decode(self):
        """
        Test decoding functionality with valid input.
        """
        # Test decoding a simple string
        self.assertEqual(self.base45.decode("%69 VDL2"), b"Hello")
        # Test decoding with padding
        self.assertEqual(self.base45.decode("U"), b"\x00")
        # Test decoding an empty string (should raise an error)
        with self.assertRaises(ValueError):
            self.base45.decode("")

    def test_invalid_characters(self):
        """
        Test decoding with invalid Base45 characters.
        """
        # Test decoding a string with invalid characters
        with self.assertRaises(ValueError):
            self.base45.decode("Hello!")

    def test_round_trip(self):
        """
        Test encoding and decoding round-trip to ensure consistency.
        """
        # Test with a simple string
        original_data = "Base45 Test"
        encoded_data = self.base45.encode(original_data)
        decoded_data = self.base45.decode(encoded_data)
        self.assertEqual(decoded_data.decode("utf-8"), original_data)

        # Test with bytes
        original_data = b"Binary Data"
        encoded_data = self.base45.encode(original_data)
        decoded_data = self.base45.decode(encoded_data)
        self.assertEqual(decoded_data, original_data)

    def test_large_input(self):
        """
        Test encoding and decoding with a large input.
        """
        original_data = "A" * 1000  # 1000-character string
        encoded_data = self.base45.encode(original_data)
        decoded_data = self.base45.decode(encoded_data)
        self.assertEqual(decoded_data.decode("utf-8"), original_data)


if __name__ == "__main__":
    unittest.main()
