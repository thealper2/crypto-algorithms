from typing import Optional


class ROT47Cipher:
    """
    A class to implement the ROT47 cipher algorithm.
    """

    def __init__(self):
        """
        Initializes the ROT47Cipher class.
        """
        pass

    def _rotate_char(self, char: str) -> Optional[str]:
        """
        Rotates a single character by 47 positions in the ASCII table.

        Args:
            char (str): The character to rotate.

        Returns:
            Optional[str]: The rotated character or None if the input is invalid.
        """
        if len(char) != 1:
            return None

        ascii_val = ord(char)
        # Rotate only printable ASCII characters (33 to 126)
        if 33 <= ascii_val <= 126:
            return chr(33 + ((ascii_val + 14) % 94))

        return char

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using the ROT47 cipher.

        Args:
            text (str): The text to encrypt.

        Returns:
            str: The encrypted text.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        return "".join([self._rotate_char(char) for char in text])

    def decrypt(self, text: str) -> str:
        """
        Decrypts the input text using the ROT47 cipher.

        Args:
            text (str): The text to decrypt

        Returns:
            str: The decrypted text.
        """
        return self.encrypt(text)
