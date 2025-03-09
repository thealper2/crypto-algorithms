from typing import List, Tuple


class PlayfairCipher:
    """
    A class to implement the Playfair cipher encryption and decryption.
    """

    def __init__(self, key: str):
        """
        Initialize the Playfair cipher with a given key.

        Args:
            key (str): The key to generate the Playfair square.
        """
        self.key = key.upper().replace(
            "J", "I"
        )  # Replace 'J' with 'I' as per Playfair rules
        self.square = self._generate_square()

    def _generate_square(self) -> List[List[str]]:
        """
        Generate the 5x5 Playfair square using the provided key.

        Returns:
            List[List[str]]: A 5x5 matrix representing the Playfair square.
        """
        key_chars = []
        for char in self.key:
            if char not in key_chars and char.isalpha():
                key_chars.append(char)

        # Fill the remaining squares with the rest of the alphabet (excluding 'J')
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in key_chars:
                key_chars.append(char)

        # Reshape into a 5x5 square
        square = [key_chars[i : i + 5] for i in range(0, 25, 5)]
        return square

    def _prepare_text(self, text: str) -> str:
        """
        Prepare the input text for encryption/decryption by:
        1. Converting to uppercase.
        2. Replacing 'J' with 'I'.
        3. Adding an 'X' between duplicate letters in a pair.
        4. Adding an 'X' if the length is odd.

        Args:
            text (str): The input text to prepare.

        Returns:
            str: The prepared text.
        """
        text = text.upper().replace("J", "I")
        prepared_text = ""

        i = 0
        while i < len(text):
            if i == len(text) - 1:
                prepared_text += text[i] + "X"  # Add 'X' if the length is odd
                break
            if text[i] == text[i + 1]:
                prepared_text += text[i] + "X"  # Add 'X' between duplicate letters
                i += 1
            else:
                prepared_text += text[i] + text[i + 1]
                i += 2

        return prepared_text

    def _find_position(self, char: str) -> Tuple[int, int]:
        """
        Find the position of a character in the Playfair square.

        Args:
            char (str): The character to find.

        Returns:
            Tuple[int, int]: The row and column indices of the character.

        Raises:
            ValueError: If the character is not found in the square.
        """
        for row in range(5):
            for col in range(5):
                if self.square[row][col] == char:
                    return (row, col)
        raise ValueError(f"Character '{char}' not found in the Playfair square.")

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using the Playfair cipher.

        Args:
            plaintext (str): The plaintext to encrypt.

        Returns:
            str: The encrypted ciphertext.
        """
        plaintext = self._prepare_text(plaintext)
        ciphertext = ""

        for i in range(0, len(plaintext), 2):
            char1, char2 = plaintext[i], plaintext[i + 1]
            row1, col1 = self._find_position(char1)
            row2, col2 = self._find_position(char2)

            if row1 == row2:
                # Same row: shift right (wrap around)
                ciphertext += (
                    self.square[row1][(col1 + 1) % 5]
                    + self.square[row2][(col2 + 1) % 5]
                )
            elif col1 == col2:
                # Same column: shift down (wrap around)
                ciphertext += (
                    self.square[(row1 + 1) % 5][col1]
                    + self.square[(row2 + 1) % 5][col2]
                )
            else:
                # Rectangle: swap columns
                ciphertext += self.square[row1][col2] + self.square[row2][col1]

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the ciphertext using the Playfair cipher.

        Args:
            ciphertext (str): The ciphertext to decrypt.

        Returns:
            str: The decrypted plaintext.
        """
        plaintext = ""

        for i in range(0, len(ciphertext), 2):
            char1, char2 = ciphertext[i], ciphertext[i + 1]
            row1, col1 = self._find_position(char1)
            row2, col2 = self._find_position(char2)

            if row1 == row2:
                # Same row: shift left (wrap around)
                plaintext += (
                    self.square[row1][(col1 - 1) % 5]
                    + self.square[row2][(col2 - 1) % 5]
                )
            elif col1 == col2:
                # Same column: shift up (wrap around)
                plaintext += (
                    self.square[(row1 - 1) % 5][col1]
                    + self.square[(row2 - 1) % 5][col2]
                )
            else:
                # Rectangle: swap columns
                plaintext += self.square[row1][col2] + self.square[row2][col1]

        return plaintext
