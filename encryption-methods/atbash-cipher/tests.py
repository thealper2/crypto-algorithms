import unittest
from atbash import AtbashCipher


class TestAtbashCipher(unittest.TestCase):
    """
    A test class for the AtbashCipher implementation.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of AtbashCipher.
        """
        self.cipher = AtbashCipher()

    def test_encrypt_valid_input(self):
        """
        Test the encryption of valid input text.
        """
        self.assertEqual(self.cipher.encrypt("HELLO"), "SVOOL")
        self.assertEqual(self.cipher.encrypt("PYTHON"), "KBGSLM")
        self.assertEqual(self.cipher.encrypt("ABC"), "ZYX")

    def test_decrypt_valid_input(self):
        """
        Test the decryption of valid input text.
        """
        self.assertEqual(self.cipher.decrypt("SVOOL"), "HELLO")
        self.assertEqual(self.cipher.decrypt("KBGSLM"), "PYTHON")
        self.assertEqual(self.cipher.decrypt("ZYX"), "ABC")

    def test_encrypt_invalid_input(self):
        """
        Test the encryption of invalid input text (non-alphabetic characters).
        """
        with self.assertRaises(ValueError):
            self.cipher.encrypt("HELLO123")
        with self.assertRaises(ValueError):
            self.cipher.encrypt("HELLO!")

    def test_decrypt_invalid_input(self):
        """
        Test the decryption of invalid input text (non-alphabetic characters).
        """
        with self.assertRaises(ValueError):
            self.cipher.decrypt("SVOOL123")
        with self.assertRaises(ValueError):
            self.cipher.decrypt("SVOOL!")

    def test_encrypt_decrypt_consistency(self):
        """
        Test the consistency of encryption and decryption.
        Encrypting and then decrypting should return the original text.
        """
        original_text = "HELLO"
        encrypted_text = self.cipher.encrypt(original_text)
        decrypted_text = self.cipher.decrypt(encrypted_text)
        self.assertEqual(original_text, decrypted_text)

    def test_case_insensitivity(self):
        """
        Test that the encryption and decryption are case-insensitive.
        """
        self.assertEqual(self.cipher.encrypt("hello"), "SVOOL")
        self.assertEqual(self.cipher.decrypt("svool"), "HELLO")


if __name__ == "__main__":
    unittest.main()
