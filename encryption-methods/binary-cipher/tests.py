import unittest
from binary_cipher import BinaryCipher


class TestBinaryCipher(unittest.TestCase):
    """
    A test class for the BinaryCipher class.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of BinaryCipher.
        """
        self.cipher = BinaryCipher()

    def test_encode_valid_text(self):
        """
        Test encoding a valid text string into binary.
        """
        input_text = "Hello"
        expected_output = "01001000 01100101 01101100 01101100 01101111"
        result = self.cipher.encode(input_text)
        self.assertEqual(result, expected_output)

    def test_decode_valid_binary(self):
        """
        Test decoding a valid binary string back into text.
        """
        input_binary = "01001000 01100101 01101100 01101100 01101111"
        expected_output = "Hello"
        result = self.cipher.decode(input_binary)
        self.assertEqual(result, expected_output)

    def test_encode_empty_text(self):
        """
        Test encoding an empty text string. This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.cipher.encode("")

    def test_decode_empty_binary(self):
        """
        Test decoding an empty binary string. This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.cipher.decode("")

    def test_decode_invalid_binary(self):
        """
        Test decoding an invalid binary string. This should raise a ValueError.
        """
        invalid_binary = "0100100 01100101 01101100 01101100 01101111"  # Missing one bit in the first byte
        with self.assertRaises(ValueError):
            self.cipher.decode(invalid_binary)

    def test_encode_decode_roundtrip(self):
        """
        Test encoding and then decoding a text string to ensure the roundtrip works correctly.
        """
        input_text = "Hello, World!"
        encoded = self.cipher.encode(input_text)
        decoded = self.cipher.decode(encoded)
        self.assertEqual(decoded, input_text)


if __name__ == "__main__":
    unittest.main()
