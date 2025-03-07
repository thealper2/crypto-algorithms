import unittest
from rot18 import ROT18Cipher


class TestROT18Cipher(unittest.TestCase):
    """
    Test cases for the ROT18Cipher class.
    """

    def setUp(self):
        """
        Set up the ROT18Cipher instance for testing.
        """
        self.cipher = ROT18Cipher()

    def test_rot13_letters(self):
        """
        Test ROT13 rotation for letters.
        """
        # Test lowercase letters
        self.assertEqual(self.cipher.encrypt("hello"), "uryyb")
        self.assertEqual(self.cipher.decrypt("uryyb"), "hello")

        # Test uppercase letters
        self.assertEqual(self.cipher.encrypt("HELLO"), "URYYB")
        self.assertEqual(self.cipher.decrypt("URYYB"), "HELLO")

    def test_rot5_numbers(self):
        """
        Test ROT5 rotation for numbers.
        """
        # Test numbers
        self.assertEqual(self.cipher.encrypt("12345"), "67890")
        self.assertEqual(self.cipher.decrypt("67890"), "12345")

    def test_rot18_mixed(self):
        """
        Test ROT18 rotation for mixed letters and numbers.
        """
        # Test mixed letters and numbers
        self.assertEqual(self.cipher.encrypt("Hello123"), "Uryyb678")
        self.assertEqual(self.cipher.decrypt("Uryyb678"), "Hello123")

    def test_non_alphanumeric(self):
        """
        Test that non-alphanumeric characters are not rotated.
        """
        # Test non-alphanumeric characters
        self.assertEqual(self.cipher.encrypt("Hello, World! 123"), "Uryyb, Jbeyq! 678")
        self.assertEqual(self.cipher.decrypt("Uryyb, Jbeyq! 678"), "Hello, World! 123")

    def test_empty_string(self):
        """
        Test that an empty string is handled correctly.
        """
        self.assertEqual(self.cipher.encrypt(""), "")
        self.assertEqual(self.cipher.decrypt(""), "")

    def test_invalid_characters(self):
        """
        Test that invalid characters (non-alphanumeric) raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.cipher._rotate_char("!")
        with self.assertRaises(ValueError):
            self.cipher._rotate_char("@")


if __name__ == "__main__":
    unittest.main()
