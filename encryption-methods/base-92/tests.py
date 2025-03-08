import unittest
from base_92 import Base92Cipher


class TestBase92(unittest.TestCase):
    """
    Test cases for the Base92 encoding and decoding functionality.
    """

    def setUp(self):
        """
        Set up the Base92 instance for testing.
        """
        self.base92 = Base92Cipher()

    def test_encode_string(self):
        """
        Test encoding a simple string.
        """
        input_data = b"Hello, World!"
        expected_output = ">OwJh>Io0Tv!8PE"
        encoded = self.base92.encode(input_data)
        self.assertEqual(encoded, expected_output)

    def test_decode_string(self):
        """
        Test decoding a Base92 encoded string.
        """
        input_data = ">OwJh>Io0Tv!8PE"
        expected_output = b"Hello, World!"
        decoded = self.base92.decode(input_data)
        self.assertEqual(decoded, expected_output)

    def test_encode_empty_string(self):
        """
        Test encoding an empty byte string.
        """
        input_data = b""
        expected_output = ""
        encoded = self.base92.encode(input_data)
        self.assertEqual(encoded, expected_output)

    def test_decode_empty_string(self):
        """
        Test decoding an empty Base92 string.
        """
        input_data = ""
        expected_output = b""
        decoded = self.base92.decode(input_data)
        self.assertEqual(decoded, expected_output)

    def test_encode_binary_data(self):
        """
        Test encoding binary data.
        """
        input_data = bytes([0x00, 0xFF, 0x55, 0xAA])
        expected_output = "!=B]"
        encoded = self.base92.encode(input_data)
        self.assertEqual(encoded, expected_output)

    def test_decode_binary_data(self):
        """
        Test decoding binary data.
        """
        input_data = "!=B]"
        expected_output = bytes([0x00, 0xFF, 0x55, 0xAA])
        decoded = self.base92.decode(input_data)
        self.assertEqual(decoded, expected_output)

    def test_encode_invalid_input_type(self):
        """
        Test encoding with invalid input type (non-bytes).
        """
        with self.assertRaises(TypeError):
            self.base92.encode("Invalid input type")

    def test_decode_invalid_input_type(self):
        """
        Test decoding with invalid input type (non-string).
        """
        with self.assertRaises(TypeError):
            self.base92.decode(b"Invalid input type")

    def test_decode_invalid_base92_characters(self):
        """
        Test decoding a string with invalid Base92 characters.
        """
        invalid_input = "Hello, World!@#"
        with self.assertRaises(ValueError):
            self.base92.decode(invalid_input)

    def test_encode_decode_roundtrip(self):
        """
        Test encoding and decoding roundtrip to ensure data integrity.
        """
        input_data = b"Test roundtrip functionality."
        encoded = self.base92.encode(input_data)
        decoded = self.base92.decode(encoded)
        self.assertEqual(decoded, input_data)


if __name__ == "__main__":
    unittest.main()
