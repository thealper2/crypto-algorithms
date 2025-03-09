import unittest
from beaufort_cipher import BeaufortCipher


class TestBeaufortCipher(unittest.TestCase):
    """
    A test class for the BeaufortCipher implementation.
    """

    def test_encryption(self):
        """
        Test encryption with a valid key and plaintext.
        """
        cipher = BeaufortCipher("KEY")
        plaintext = "HELLO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "RIJVS")

    def test_decryption(self):
        """
        Test decryption with a valid key and ciphertext.
        """
        cipher = BeaufortCipher("KEY")
        ciphertext = "RIJVS"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, "HELLO")

    def test_encryption_with_non_alphabetic_characters(self):
        """
        Test encryption with non-alphabetic characters in the plaintext.
        Non-alphabetic characters should remain unchanged.
        """
        cipher = BeaufortCipher("KEY")
        plaintext = "HELLO, WORLD!"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "RIJVS, UMDVS!")

    def test_decryption_with_non_alphabetic_characters(self):
        """
        Test decryption with non-alphabetic characters in the ciphertext.
        Non-alphabetic characters should remain unchanged.
        """
        cipher = BeaufortCipher("KEY")
        ciphertext = "RIJVS, UMDVS!"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, "HELLO, WORLD!")

    def test_key_with_non_alphabetic_characters(self):
        """
        Test initialization with a key containing non-alphabetic characters.
        Should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            BeaufortCipher("KEY123")

    def test_empty_key(self):
        """
        Test initialization with an empty key.
        Should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            BeaufortCipher("")

    def test_empty_text(self):
        """
        Test encryption and decryption with an empty text.
        Should return an empty string.
        """
        cipher = BeaufortCipher("KEY")
        self.assertEqual(cipher.encrypt(""), "")
        self.assertEqual(cipher.decrypt(""), "")

    def test_case_insensitivity(self):
        """
        Test that the cipher is case-insensitive for input text.
        The output should always be uppercase.
        """
        cipher = BeaufortCipher("KEY")
        plaintext = "HeLlO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "DANZQ")

    def test_long_key(self):
        """
        Test encryption and decryption with a key longer than the text.
        """
        cipher = BeaufortCipher("LONGKEY")
        plaintext = "HELLO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "EKCVW")
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, "HELLO")

    def test_long_text(self):
        """
        Test encryption and decryption with a text longer than the key.
        """
        cipher = BeaufortCipher("KEY")
        plaintext = "HELLOWORLD"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "RIJVSUMDVS")
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, "HELLOWORLD")


if __name__ == "__main__":
    unittest.main()
