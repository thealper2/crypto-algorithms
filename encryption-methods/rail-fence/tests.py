import unittest
from rail_fence import RailFenceCipher


class TestRailFenceCipher(unittest.TestCase):
    """
    A test class for the RailFenceCipher class.
    This class tests the encryption and decryption functionality of the Rail Fence Cipher.
    """

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid input.
        """
        cipher = RailFenceCipher(3)
        result = cipher.encrypt("HELLO")
        self.assertEqual(result, "HOELL", "Encryption failed for valid input.")

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid input.
        """
        cipher = RailFenceCipher(3)
        result = cipher.decrypt("HOELL")
        self.assertEqual(result, "HELLO", "Decryption failed for valid input.")

    def test_encrypt_empty_string(self):
        """
        Test encryption with an empty string.
        """
        cipher = RailFenceCipher(3)
        result = cipher.encrypt("")
        self.assertEqual(result, "", "Encryption failed for empty string.")

    def test_decrypt_empty_string(self):
        """
        Test decryption with an empty string.
        """
        cipher = RailFenceCipher(3)
        result = cipher.decrypt("")
        self.assertEqual(result, "", "Decryption failed for empty string.")

    def test_encrypt_invalid_rails(self):
        """
        Test encryption with invalid number of rails (less than 2).
        """
        with self.assertRaises(ValueError):
            RailFenceCipher(0)  # Should raise ValueError

    def test_decrypt_invalid_rails(self):
        """
        Test decryption with invalid number of rails (less than 2).
        """
        with self.assertRaises(ValueError):
            RailFenceCipher(-1)  # Should raise ValueError

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting returns the original text.
        """
        cipher = RailFenceCipher(4)
        original_text = "RAILFENCECIPHER"
        encrypted = cipher.encrypt(original_text)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(
            original_text, decrypted, "Encryption and decryption are not consistent."
        )

    def test_encrypt_special_characters(self):
        """
        Test encryption with special characters and spaces.
        """
        cipher = RailFenceCipher(3)
        result = cipher.encrypt("HELLO WORLD!")
        self.assertEqual(
            result, "HOREL OL!LWD", "Encryption failed for special characters."
        )

    def test_decrypt_special_characters(self):
        """
        Test decryption with special characters and spaces.
        """
        cipher = RailFenceCipher(3)
        result = cipher.decrypt("HOREL OL!LWD")
        self.assertEqual(
            result, "HELLO WORLD!", "Decryption failed for special characters."
        )


if __name__ == "__main__":
    unittest.main()
