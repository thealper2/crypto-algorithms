import unittest
from md4 import MD4


class TestMD4(unittest.TestCase):
    """
    Test suite for the MD4 hashing algorithm implementation.
    """

    def test_empty_string(self):
        """
        Test MD4 hash of an empty string.
        The expected hash is the MD4 hash of an empty input.
        """
        md4 = MD4()
        result = md4.hash(b"")
        expected = bytes.fromhex("31d6cfe0d16ae931b73c59d7e0c089c0")
        self.assertEqual(result, expected, "MD4 hash of empty string is incorrect.")

    def test_single_character(self):
        """
        Test MD4 hash of a single character.
        The expected hash is the MD4 hash of the character 'a'.
        """
        md4 = MD4()
        result = md4.hash(b"a")
        expected = bytes.fromhex("bde52cb31de33e46245e05fbdbd6fb24")
        self.assertEqual(result, expected, "MD4 hash of 'a' is incorrect.")

    def test_short_string(self):
        """
        Test MD4 hash of a short string.
        The expected hash is the MD4 hash of the string 'hello'.
        """
        md4 = MD4()
        result = md4.hash(b"hello")
        expected = bytes.fromhex("866437cb7a794bce2b727acc0362ee27")
        self.assertEqual(result, expected, "MD4 hash of 'hello' is incorrect.")

    def test_long_string(self):
        """
        Test MD4 hash of a longer string.
        The expected hash is the MD4 hash of the string 'The quick brown fox jumps over the lazy dog'.
        """
        md4 = MD4()
        result = md4.hash(b"The quick brown fox jumps over the lazy dog")
        expected = bytes.fromhex("1bee69a46ba811185c194762abaeae90")
        self.assertEqual(result, expected, "MD4 hash of the long string is incorrect.")

    def test_string_with_special_characters(self):
        """
        Test MD4 hash of a string containing special characters.
        The expected hash is the MD4 hash of the string 'password123!@#'.
        """
        md4 = MD4()
        result = md4.hash(b"password123!@#")
        expected = bytes.fromhex("1bfc985c5c1d736cabb2abe043e55884")
        self.assertEqual(result, expected, "MD4 hash of 'password123!@#' is incorrect.")

    def test_large_input(self):
        """
        Test MD4 hash of a large input (1 MB of 'a' characters).
        This ensures the implementation can handle large inputs correctly.
        """
        md4 = MD4()
        large_input = b"a" * (1024)
        result = md4.hash(large_input)
        expected = bytes.fromhex("0eab1d76a65a97bf3657150b586e4155")
        self.assertEqual(result, expected, "MD4 hash of large input is incorrect.")

    def test_invalid_input_type(self):
        """
        Test that passing a non-bytes input raises a TypeError.
        MD4.hash() expects bytes as input.
        """
        md4 = MD4()
        with self.assertRaises(
            TypeError, msg="MD4.hash() should raise TypeError for non-bytes input."
        ):
            md4.hash("invalid input")  # Passing a string instead of bytes


if __name__ == "__main__":
    unittest.main()
