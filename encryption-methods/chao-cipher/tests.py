import unittest
from chao_cipher import ChaoCipher


class TestChaoCipher(unittest.TestCase):
    """
    Test cases for the ChaoCipher class.
    """

    def setUp(self):
        """
        Set up test fixtures. This method is called before each test.
        """
        # Define valid alphabets for testing
        self.left_alphabet = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
        self.right_alphabet = "PTLNBQDEOYSFAVZKGJRIHWXUMC"
        self.cipher = ChaoCipher(self.left_alphabet, self.right_alphabet)

    def test_initialization_valid_alphabets(self):
        """
        Test initialization with valid alphabets.
        """
        # Check if the alphabets are correctly assigned
        self.assertEqual(self.cipher.left_alphabet, self.left_alphabet)
        self.assertEqual(self.cipher.right_alphabet, self.right_alphabet)

    def test_initialization_invalid_alphabets(self):
        """
        Test initialization with invalid alphabets (unequal length or duplicates).
        """
        # Test with alphabets of unequal length
        with self.assertRaises(ValueError):
            ChaoCipher("ABC", "DEFG")

        # Test with alphabets containing duplicate characters
        with self.assertRaises(ValueError):
            ChaoCipher("AABC", "DEFG")

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid input.
        """
        plaintext = "HELLO"
        expected_ciphertext = "WMUUD"
        ciphertext = self.cipher.encrypt(plaintext)
        self.assertEqual(ciphertext, expected_ciphertext)

    def test_encrypt_invalid_input(self):
        """
        Test encryption with invalid input (characters not in the right alphabet).
        """
        plaintext = "HELLO123"
        with self.assertRaises(ValueError):
            self.cipher.encrypt(plaintext)

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid input.
        """
        ciphertext = "WMUUD"
        expected_plaintext = "HELLO"
        plaintext = self.cipher.decrypt(ciphertext)
        self.assertEqual(plaintext, expected_plaintext)

    def test_decrypt_invalid_input(self):
        """
        Test decryption with invalid input (characters not in the left alphabet).
        """
        ciphertext = "AXEEH123"
        with self.assertRaises(ValueError):
            self.cipher.decrypt(ciphertext)

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting a message returns the original message.
        """
        plaintext = "HELLO"
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted_text = self.cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, plaintext)

    def test_permute_alphabet(self):
        """
        Test the _permute_alphabet helper method.
        """
        alphabet = "ABCDEF"
        index = 2
        permuted_alphabet = self.cipher._permute_alphabet(alphabet, index)
        self.assertEqual(permuted_alphabet, "CDEFAB")

    def test_shift_alphabet(self):
        """
        Test the _shift_alphabet helper method.
        """
        alphabet = "ABCDEF"
        shifted_alphabet = self.cipher._shift_alphabet(alphabet)
        self.assertEqual(shifted_alphabet, "ACDEFB")


if __name__ == "__main__":
    unittest.main()
