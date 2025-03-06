import unittest
from caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    """
    Test cases for the CaesarCipher class.
    """

    def test_encrypt_uppercase(self):
        """
        Test encryption with uppercase letters.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.encrypt("HELLO")
        self.assertEqual(result, "KHOOR", "Uppercase encryption failed.")

    def test_encrypt_lowercase(self):
        """
        Test encryption with lowercase letters.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.encrypt("hello")
        self.assertEqual(result, "khoor", "Lowercase encryption failed.")

    def test_encrypt_with_non_alpha(self):
        """
        Test encryption with non-alphabetic characters.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.encrypt("Hello, World! 123")
        self.assertEqual(
            result,
            "Khoor, Zruog! 123",
            "Non-alphabetic characters were not handled correctly.",
        )

    def test_decrypt_uppercase(self):
        """
        Test decryption with uppercase letters.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.decrypt("KHOOR", shift=3)
        self.assertEqual(result, "HELLO", "Uppercase decryption failed.")

    def test_decrypt_lowercase(self):
        """
        Test decryption with lowercase letters.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.decrypt("khoor", shift=3)
        self.assertEqual(result, "hello", "Lowercase decryption failed.")

    def test_decrypt_with_non_alpha(self):
        """
        Test decryption with non-alphabetic characters.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.decrypt("Khoor, Zruog! 123", shift=3)
        self.assertEqual(
            result,
            "Hello, World! 123",
            "Non-alphabetic characters were not handled correctly.",
        )

    def test_brute_force_decrypt(self):
        """
        Test brute-force decryption by verifying that the correct shift is found.
        """
        cipher = CaesarCipher(shift=5)
        encrypted_text = cipher.encrypt("Hello")
        # Brute-force should find the correct shift (5) and return the original text.
        result = cipher.decrypt(encrypted_text)
        self.assertIn("Shift 5: Hello", result)

    def test_encrypt_with_custom_shift(self):
        """
        Test encryption with a custom shift value.
        """
        cipher = CaesarCipher(shift=10)
        result = cipher.encrypt("Hello")
        self.assertEqual(result, "Rovvy", "Encryption with custom shift failed.")

    def test_decrypt_with_custom_shift(self):
        """
        Test decryption with a custom shift value.
        """
        cipher = CaesarCipher(shift=10)
        result = cipher.decrypt("Rovvy", shift=10)
        self.assertEqual(result, "Hello", "Decryption with custom shift failed.")

    def test_encrypt_empty_string(self):
        """
        Test encryption with an empty string.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.encrypt("")
        self.assertEqual(result, "", "Encryption of an empty string failed.")

    def test_decrypt_empty_string(self):
        """
        Test decryption with an empty string.
        """
        cipher = CaesarCipher(shift=3)
        result = cipher.decrypt("", shift=3)
        self.assertEqual(result, "", "Decryption of an empty string failed.")

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting returns the original text.
        """
        cipher = CaesarCipher(shift=7)
        original_text = "Caesar Cipher"
        encrypted_text = cipher.encrypt(original_text)
        decrypted_text = cipher.decrypt(encrypted_text, shift=7)
        self.assertEqual(
            original_text,
            decrypted_text,
            "Encryption and decryption are not consistent.",
        )


if __name__ == "__main__":
    unittest.main()
