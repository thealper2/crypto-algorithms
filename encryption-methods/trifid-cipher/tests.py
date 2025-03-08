import unittest
from trifid import TrifidCipher


class TestTrifidCipher(unittest.TestCase):
    """
    A test class for the TrifidCipher implementation.
    This class tests the encryption, decryption, and error handling of the TrifidCipher class.
    """

    def setUp(self) -> None:
        """
        Set up the TrifidCipher instance for testing.
        This method is called before each test case.
        """
        self.cipher = TrifidCipher()

    def test_encrypt_valid_input(self) -> None:
        """
        Test encryption with valid input.
        Ensures that the encryption process works correctly for valid plaintext.
        """
        plaintext = "HELLO"
        expected_ciphertext = "ANQMF"  # Expected result based on the cube configuration
        result = self.cipher.encrypt(plaintext)
        self.assertEqual(result, expected_ciphertext)

    def test_decrypt_valid_input(self) -> None:
        """
        Test decryption with valid input.
        Ensures that the decryption process works correctly for valid ciphertext.
        """
        ciphertext = "ANQMF"
        expected_plaintext = "HELLO"  # Expected result based on the cube configuration
        result = self.cipher.decrypt(ciphertext)
        self.assertEqual(result, expected_plaintext)

    def test_encrypt_decrypt_roundtrip(self) -> None:
        """
        Test encryption followed by decryption.
        Ensures that decrypting an encrypted message returns the original plaintext.
        """
        plaintext = "PYTHON"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_encrypt_invalid_input(self) -> None:
        """
        Test encryption with invalid input.
        Ensures that the encryption process raises a ValueError for characters not in the cube.
        """
        plaintext = "HELLO123"  # '1' and '2' are not in the cube
        with self.assertRaises(ValueError):
            self.cipher.encrypt(plaintext)

    def test_decrypt_invalid_input(self) -> None:
        """
        Test decryption with invalid input.
        Ensures that the decryption process raises a ValueError for characters not in the cube.
        """
        ciphertext = "ANQMF123"  # '1' and '2' are not in the cube
        with self.assertRaises(ValueError):
            self.cipher.decrypt(ciphertext)

    def test_encrypt_empty_input(self) -> None:
        """
        Test encryption with empty input.
        Ensures that the encryption process handles empty strings gracefully.
        """
        plaintext = ""
        result = self.cipher.encrypt(plaintext)
        self.assertEqual(result, "")

    def test_decrypt_empty_input(self) -> None:
        """
        Test decryption with empty input.
        Ensures that the decryption process handles empty strings gracefully.
        """
        ciphertext = ""
        result = self.cipher.decrypt(ciphertext)
        self.assertEqual(result, "")

    def test_encrypt_with_spaces(self) -> None:
        """
        Test encryption with spaces in the input.
        Ensures that spaces are removed before encryption.
        """
        plaintext = "HELLO WORLD"
        expected_ciphertext = "ANQMFXUZQ"  # Expected result after removing spaces
        result = self.cipher.encrypt(plaintext)
        self.assertEqual(result, expected_ciphertext)

    def test_decrypt_with_spaces(self) -> None:
        """
        Test decryption with spaces in the input.
        Ensures that spaces are removed before decryption.
        """
        ciphertext = "ANQMF XUZQ"  # Spaces should be ignored
        expected_plaintext = "HELLOWORLD"  # Expected result after removing spaces
        result = self.cipher.decrypt(ciphertext)
        self.assertEqual(result, expected_plaintext)

    def test_encrypt_case_insensitivity(self) -> None:
        """
        Test encryption with mixed-case input.
        Ensures that the encryption process is case-insensitive.
        """
        plaintext = "Hello"
        expected_ciphertext = "ANQMF"  # Expected result for "HELLO"
        result = self.cipher.encrypt(plaintext)
        self.assertEqual(result, expected_ciphertext)

    def test_decrypt_case_insensitivity(self) -> None:
        """
        Test decryption with mixed-case input.
        Ensures that the decryption process is case-insensitive.
        """
        ciphertext = "anqmf"
        expected_plaintext = "HELLO"  # Expected result for "ANQMF"
        result = self.cipher.decrypt(ciphertext)
        self.assertEqual(result, expected_plaintext)


if __name__ == "__main__":
    unittest.main()
