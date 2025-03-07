import unittest
from rot13 import ROT13Cipher


class TestRot13Cipher(unittest.TestCase):
    """
    A test class for the Rot13Cipher class.
    This class contains unit tests to verify the functionality of the ROT13 encryption and decryption.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of Rot13Cipher.
        This method runs before each test case.
        """
        self.cipher = ROT13Cipher()

    def test_encrypt_decrypt_lowercase(self):
        """
        Test ROT13 encryption and decryption with lowercase letters.
        """
        # Test encryption
        self.assertEqual(self.cipher.encrypt_decrypt("hello"), "uryyb")
        # Test decryption (ROT13 is its own inverse)
        self.assertEqual(self.cipher.encrypt_decrypt("uryyb"), "hello")

    def test_encrypt_decrypt_uppercase(self):
        """
        Test ROT13 encryption and decryption with uppercase letters.
        """
        # Test encryption
        self.assertEqual(self.cipher.encrypt_decrypt("HELLO"), "URYYB")
        # Test decryption (ROT13 is its own inverse)
        self.assertEqual(self.cipher.encrypt_decrypt("URYYB"), "HELLO")

    def test_encrypt_decrypt_mixed_case(self):
        """
        Test ROT13 encryption and decryption with mixed-case letters.
        """
        # Test encryption
        self.assertEqual(self.cipher.encrypt_decrypt("Hello World"), "Uryyb Jbeyq")
        # Test decryption (ROT13 is its own inverse)
        self.assertEqual(self.cipher.encrypt_decrypt("Uryyb Jbeyq"), "Hello World")

    def test_encrypt_decrypt_non_alphabetic(self):
        """
        Test ROT13 encryption and decryption with non-alphabetic characters.
        Non-alphabetic characters should remain unchanged.
        """
        # Test encryption
        self.assertEqual(self.cipher.encrypt_decrypt("123!@#"), "123!@#")
        # Test decryption (ROT13 is its own inverse)
        self.assertEqual(self.cipher.encrypt_decrypt("123!@#"), "123!@#")

    def test_encrypt_decrypt_empty_string(self):
        """
        Test ROT13 encryption and decryption with an empty string.
        An empty string should return an empty string.
        """
        self.assertEqual(self.cipher.encrypt_decrypt(""), "")

    def test_encrypt_decrypt_invalid_input(self):
        """
        Test ROT13 encryption and decryption with invalid input (non-string).
        The method should return None and handle the error gracefully.
        """
        # Test with integer input
        self.assertIsNone(self.cipher.encrypt_decrypt(123))
        # Test with list input
        self.assertIsNone(self.cipher.encrypt_decrypt(["hello"]))


if __name__ == "__main__":
    unittest.main()
