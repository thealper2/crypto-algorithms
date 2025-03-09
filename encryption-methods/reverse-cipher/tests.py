import unittest
from reverse_cipher import ReverseCipher


class TestReverseCipher(unittest.TestCase):
    """
    A test class for the ReverseCipher implementation.
    """

    def test_reverse_empty_string(self):
        """
        Test reversing an empty string.
        The result should also be an empty string.
        """
        text = ""
        cipher = ReverseCipher()
        self.assertEqual(cipher.encrypt(text), "")

    def test_reverse_single_character(self):
        """
        Test reversing a single-character string.
        The result should be the same as the input.

        """
        text = "a"
        cipher = ReverseCipher()
        self.assertEqual(cipher.encrypt(text), "a")

    def test_reverse_normal_string(self):
        """
        Test reversing a normal string.
        """
        text = "Hello, World!"
        cipher = ReverseCipher()
        self.assertEqual(cipher.encrypt(text), "!dlroW ,olleH")

    def test_reverse_string_with_spaces(self):
        """
        Test reversing a string that contains spaces.
        """
        text = "Python is fun"
        cipher = ReverseCipher()
        self.assertEqual(cipher.encrypt(text), "nuf si nohtyP")

    def test_reverse_special_characters(self):
        """
        Test reversing a string with special characters.
        """
        text = "123@#abc"
        cipher = ReverseCipher()
        self.assertEqual(cipher.encrypt(text), "cba#@321")

    def test_encrypt_normal_string(self):
        """
        Test encrypting a normal string using the ReverseCipher.
        """
        text = "Hello, World!"
        cipher = ReverseCipher()
        self.assertEqual(cipher.encrypt(text), "!dlroW ,olleH")

    def test_decrypt_normal_string(self):
        """
        Test decrypting a reversed string using the ReverseCipher.
        """
        text = "!dlroW ,olleH"
        cipher = ReverseCipher()
        self.assertEqual(cipher.decrypt(text), "Hello, World!")

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting returns the original string.
        """
        original_text = "Python is awesome"
        cipher = ReverseCipher()
        encrypted_text = cipher.encrypt(original_text)
        cipher = ReverseCipher()
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, original_text)


if __name__ == "__main__":
    unittest.main()
