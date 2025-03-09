import unittest
from octal_cipher import OctalCipher


class TestOctalCipher(unittest.TestCase):
    """
    A test class for the OctalCipher implementation.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of OctalCipher.
        """
        self.cipher = OctalCipher()

    def test_encode_valid_input(self):
        """
        Test the encode method with valid input.
        """
        input_text = "Hello"
        expected_output = "110 145 154 154 157"
        result = self.cipher.encode(input_text)
        self.assertEqual(result, expected_output)

    def test_encode_invalid_input(self):
        """
        Test the encode method with invalid input (non-string).
        """
        with self.assertRaises(ValueError):
            self.cipher.encode(123)  # Passing an integer instead of a string

    def test_decode_valid_input(self):
        """
        Test the decode method with valid input.
        """
        input_octal = "110 145 154 154 157"
        expected_output = "Hello"
        result = self.cipher.decode(input_octal)
        self.assertEqual(result, expected_output)

    def test_decode_invalid_input(self):
        """
        Test the decode method with invalid input (non-string).
        """
        with self.assertRaises(ValueError):
            self.cipher.decode(123)  # Passing an integer instead of a string

    def test_decode_invalid_octal(self):
        """
        Test the decode method with an invalid octal string.
        """
        invalid_octal = "110 999 154"  # '999' is not a valid octal number
        with self.assertRaises(ValueError):
            self.cipher.decode(invalid_octal)

    def test_text_to_octal_and_back(self):
        """
        Test encoding and decoding together to ensure consistency.
        """
        input_text = "Python"
        octal_result = self.cipher.encode(input_text)
        text_result = self.cipher.decode(octal_result)
        self.assertEqual(input_text, text_result)

    def test_empty_string(self):
        """
        Test the text_to_octal and octal_to_text methods with an empty string.
        """
        input_text = ""
        octal_result = self.cipher.encode(input_text)
        self.assertEqual(octal_result, "")
        text_result = self.cipher.decode(octal_result)
        self.assertEqual(text_result, "")


if __name__ == "__main__":
    unittest.main()
