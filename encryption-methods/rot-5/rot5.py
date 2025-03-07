class ROT5Cipher:
    """
    A class to implement the ROT5 cipher, which rotates digits by 5 positions.
    Only digits (0-9) are affected; other characters remain unchanged.
    """

    def __init__(self):
        """
        Initialize the ROT5 cipher.
        """
        self.rotation = 5
        self.digit_range = 10  # Digits 0-9

    def _rotate_digit(self, char: str) -> str:
        """
        Rotate a single digit character by 5 positions.

        Args:
            char (str): A single character (must be a digit).

        Returns:
            str: The rotated digit character.

        Raises:
            ValueError: If the input is not a single digit.
        """
        if not char.isdigit() or len(char) != 1:
            raise ValueError("Input must be a single digit (0-9).")

        # Convert the character to its integer value, rotate and wrap around using modula 10
        rotated_digit = (int(char) + self.rotation) % self.digit_range
        return str(rotated_digit)

    def encrypt(self, text: str) -> str:
        """
        Encrypt the input text using ROT5 cipher.

        Args:
            text (str): The input text to encrypt.

        Returns:
            str: The encrypted text.
        """
        encrypted_text = []
        for char in text:
            if char.isdigit():
                encrypted_text.append(self._rotate_digit(char))
            else:
                encrypted_text.append(char)

        return "".join(encrypted_text)

    def decrypt(self, text: str) -> str:
        """
        Decrypt the input text using ROT5 cipher.

        Args:
            text (str): The input text to decrypt.

        Returns:
            str: The decrypted text.
        """
        # Decryption is the same as encryption for ROT5.
        return self.encrypt(text)
