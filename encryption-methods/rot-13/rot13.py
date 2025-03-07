import string
from typing import Optional


class ROT13Cipher:
    """
    A class to handle ROT13 encryption and decryption.
    """

    def __init__(self):
        """
        Initializes the ROT13 translation table for both lowercase and uppercase letters.
        """
        self.rot13_table = str.maketrans(
            string.ascii_lowercase + string.ascii_uppercase,
            string.ascii_lowercase[13:]
            + string.ascii_lowercase[:13]
            + string.ascii_uppercase[13:]
            + string.ascii_uppercase[:13],
        )

    def encrypt_decrypt(self, text: str) -> Optional[str]:
        """
        Encrypts or decrypts the input text using the ROT13 cipher.

        Args:
            text (str): The input text to be encrypted or decrypted.

        Returns:
            Optional[str]: The transformed text or None if an error occurs.
        """
        try:
            if not isinstance(text, str):
                raise ValueError("Input must be a string.")

            return text.translate(self.rot13_table)

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
