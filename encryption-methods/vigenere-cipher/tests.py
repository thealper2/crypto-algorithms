import unittest
from vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    """
    A test class for the VigenereCipher class.
    """

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid plaintext and key.
        """
        cipher = VigenereCipher("KEY")
        plaintext = "HELLO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(
            encrypted_text, "RIJVS"
        )  # Expected output for "HELLO" with key "KEY"

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid ciphertext and key.
        """
        cipher = VigenereCipher("KEY")
        ciphertext = "RIJVS"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(
            decrypted_text, "HELLO"
        )  # Expected output for "RIJVS" with key "KEY"

    def test_encrypt_with_non_alphabetic_characters(self):
        """
        Test encryption with plaintext containing non-alphabetic characters.
        """
        cipher = VigenereCipher("KEY")
        plaintext = "HELLO, WORLD!"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(
            encrypted_text, "RIJVS, UYVJN!"
        )  # Non-alphabetic characters should remain unchanged

    def test_decrypt_with_non_alphabetic_characters(self):
        """
        Test decryption with ciphertext containing non-alphabetic characters.
        """
        cipher = VigenereCipher("KEY")
        ciphertext = "RIJVS, UYVJN!"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(
            decrypted_text, "HELLO, WORLD!"
        )  # Non-alphabetic characters should remain unchanged

    def test_encrypt_empty_plaintext(self):
        """
        Test encryption with empty plaintext. Should raise a ValueError.
        """
        cipher = VigenereCipher("KEY")
        with self.assertRaises(ValueError):
            cipher.encrypt("")

    def test_decrypt_empty_ciphertext(self):
        """
        Test decryption with empty ciphertext. Should raise a ValueError.
        """
        cipher = VigenereCipher("KEY")
        with self.assertRaises(ValueError):
            cipher.decrypt("")

    def test_encrypt_invalid_key(self):
        """
        Test initialization with an invalid key (non-alphabetic or empty). Should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            VigenereCipher("123")  # Non-alphabetic key
        with self.assertRaises(ValueError):
            VigenereCipher("")  # Empty key

    def test_case_insensitivity(self):
        """
        Test that encryption and decryption are case-insensitive for both plaintext and key.
        """
        cipher = VigenereCipher("kEy")
        plaintext = "HeLlO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(
            encrypted_text, "RIJVS"
        )  # Should be the same as uppercase input
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, "HELLO")  # Should return uppercase result

    def test_long_key(self):
        """
        Test encryption and decryption with a key longer than the plaintext.
        """
        cipher = VigenereCipher("LONGKEY")
        plaintext = "HELLO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(
            encrypted_text, "SSYRY"
        )  # Expected output for "HELLO" with key "LONGKEY"
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, "HELLO")

    def test_key_wrapping(self):
        """
        Test that the key wraps around correctly when it is shorter than the plaintext.
        """
        cipher = VigenereCipher("KEY")
        plaintext = "HELLOWORLD"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "RIJVSUYVJN")  # Key should wrap around
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, "HELLOWORLD")


if __name__ == "__main__":
    unittest.main()
