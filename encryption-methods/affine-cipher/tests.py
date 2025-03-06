import unittest
from affine_cipher import AffineCipher


class TestAffineCipher(unittest.TestCase):
    """
    A test class for the AffineCipher class.
    This class contains unit tests to verify the functionality of the AffineCipher encryption and decryption methods.
    """

    def test_mod_inverse_valid(self):
        """
        Test the mod_inverse method with valid inputs.
        Verifies that the modular inverse is correctly calculated.
        """
        cipher = AffineCipher()
        self.assertEqual(cipher.mod_inverse(5, 26), 21)  # 5 * 21 = 105 ≡ 1 mod 26
        self.assertEqual(cipher.mod_inverse(3, 26), 9)  # 3 * 9 = 27 ≡ 1 mod 26

    def test_mod_inverse_invalid(self):
        """
        Test the mod_inverse method with invalid inputs.
        Verifies that the method returns None when no modular inverse exists.
        """
        cipher = AffineCipher()
        self.assertIsNone(cipher.mod_inverse(2, 26))  # 2 and 26 are not coprime
        self.assertIsNone(cipher.mod_inverse(13, 26))  # 13 and 26 are not coprime

    def test_encrypt_valid(self):
        """
        Test the encrypt method with valid inputs.
        Verifies that the encryption produces the correct ciphertext.
        """
        cipher = AffineCipher(a=5, b=8)
        self.assertEqual(cipher.encrypt("HELLO"), "RCLLA")  # Known result for a=5, b=8
        self.assertEqual(cipher.encrypt("WORLD"), "OAPLX")  # Known result for a=5, b=8

    def test_decrypt_valid(self):
        """
        Test the decrypt method with valid inputs.
        Verifies that the decryption produces the correct plaintext.
        """
        cipher = AffineCipher(a=5, b=8)
        self.assertEqual(
            cipher.decrypt("RCLLA", 5, 8), "HELLO"
        )  # Decrypt "RCLLA" with a=5, b=8
        self.assertEqual(
            cipher.decrypt("OAPLX", 5, 8), "WORLD"
        )  # Decrypt "OAPLX" with a=5, b=8

    def test_encrypt_invalid_key(self):
        """
        Test the encrypt method with an invalid key.
        Verifies that a ValueError is raised when the key 'a' is not coprime with 26.
        """
        with self.assertRaises(ValueError):
            cipher = AffineCipher(a=2, b=8)  # 2 is not coprime with 26
            cipher.encrypt("HELLO")

    def test_decrypt_invalid_key(self):
        """
        Test the decrypt method with an invalid key.
        Verifies that a ValueError is raised when the key 'a' is not coprime with 26.
        """
        with self.assertRaises(ValueError):
            cipher = AffineCipher(a=2, b=8)  # 2 is not coprime with 26
            cipher.decrypt("OAPLX", 2, 8)

    def test_non_alpha_characters(self):
        """
        Test the encrypt and decrypt methods with non-alphabetic characters.
        Verifies that non-alphabetic characters are left unchanged.
        """
        cipher = AffineCipher(a=5, b=8)
        encrypted = cipher.encrypt("HELLO, WORLD!")
        self.assertEqual(encrypted, "RCLLA, OAPLX!")
        decrypted = cipher.decrypt("RCLLA, OAPLX!", 5, 8)
        self.assertEqual(decrypted, "HELLO, WORLD!")


if __name__ == "__main__":
    unittest.main()
