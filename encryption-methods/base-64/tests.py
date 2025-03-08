import unittest
from base_64 import Base64Cipher


class TestBase64Cipher(unittest.TestCase):
    """
    Test suite for the Base64Cipher class.
    """

    def setUp(self):
        """
        Set up the Base64Cipher instance for testing.
        """
        self.cipher = Base64Cipher()

    def test_encode_basic(self):
        """
        Test encoding basic strings.
        """
        self.assertEqual(self.cipher.encode("Hello"), "SGVsbG8=")
        self.assertEqual(self.cipher.encode("Python"), "UHl0aG9u")
        self.assertEqual(self.cipher.encode("Base64"), "QmFzZTY0")

    def test_encode_empty_string(self):
        """
        Test encoding an empty string.
        """
        self.assertEqual(self.cipher.encode(""), "")

    def test_encode_special_characters(self):
        """
        Test encoding strings with special characters.
        """
        self.assertEqual(self.cipher.encode("Hello, World!"), "SGVsbG8sIFdvcmxkIQ==")
        self.assertEqual(self.cipher.encode("123!@#"), "MTIzIUAj")

    def test_encode_bytes(self):
        """
        Test encoding bytes input.
        """
        self.assertEqual(self.cipher.encode(b"Hello"), "SGVsbG8=")
        self.assertEqual(self.cipher.encode(b"\x00\x01\x02"), "AAEC")

    def test_encode_invalid_input(self):
        """
        Test encoding with invalid input types.
        """
        with self.assertRaises(TypeError):
            self.cipher.encode(123)  # Integer input
        with self.assertRaises(TypeError):
            self.cipher.encode([1, 2, 3])  # List input

    def test_decode_basic(self):
        """
        Test decoding basic Base64 strings.
        """
        self.assertEqual(self.cipher.decode("SGVsbG8="), b"Hello")
        self.assertEqual(self.cipher.decode("UHl0aG9u"), b"Python")
        self.assertEqual(self.cipher.decode("QmFzZTY0"), b"Base64")

    def test_decode_empty_string(self):
        """
        Test decoding an empty Base64 string.
        """
        self.assertEqual(self.cipher.decode(""), b"")

    def test_decode_special_characters(self):
        """
        Test decoding Base64 strings with special characters.
        """
        self.assertEqual(self.cipher.decode("SGVsbG8sIFdvcmxkIQ=="), b"Hello, World!")
        self.assertEqual(self.cipher.decode("MTIzIUAj"), b"123!@#")

    def test_decode_invalid_length(self):
        """
        Test decoding Base64 strings with invalid lengths.
        """
        with self.assertRaises(ValueError):
            self.cipher.decode("SGVsbG8")  # Length not a multiple of 4

    def test_decode_invalid_characters(self):
        """
        Test decoding Base64 strings with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.cipher.decode("SGVsbG8$")  # Invalid character '$'

    def test_encode_decode_roundtrip(self):
        """
        Test encoding and decoding roundtrip to ensure consistency.
        """
        test_cases = [
            "Hello, World!",
            "Python",
            "123!@#",
            "Base64",
            "Special characters: !@#$%^&*()",
            "",
        ]
        for case in test_cases:
            encoded = self.cipher.encode(case)
            decoded = self.cipher.decode(encoded)
            self.assertEqual(decoded.decode("utf-8"), case)


if __name__ == "__main__":
    unittest.main()
