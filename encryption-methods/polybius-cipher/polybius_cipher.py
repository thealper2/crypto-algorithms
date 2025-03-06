from typing import Dict, Tuple


class PolybiusCipher:
    """
    A class to handle encryption and description using the Polybius cipher.

    The Polybius Square is a grid of 5x5 containing all letters of the alphabet (I and J share the same cell).
    This class provides methods to create the square, encrypt plaintext and decrypt ciphertext.
    """

    def __init__(self):
        """
        Initializes the PolybiusCipher class by generating the Polybius square and its coordinate mappings.
        """
        self.square, self.coordinates = self._create_polybius_square()

    def _create_polybius_square(
        self,
    ) -> Tuple[Dict[str, Tuple[int, int]], Dict[Tuple[int, int], str]]:
        """
        Creates the Polybius square and its coordinate mappings.

        Returns:
            Tuple[Dict[str, Tuple[int, int]], Dict[Tuple[int, int], str]:
                - A dictionary mapping letters to their coordinates in the square.
                - A dictionary mapping coordinates to their corresponding letters.
        """
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: 'J' is omitted, as 'I' and 'J' share the same position
        square = {}
        index = 0

        # Generate the 5x5 square
        for row in range(1, 6):
            for col in range(1, 6):
                square[alphabet[index]] = (row, col)
                index += 1

        # Create the reverse mapping for coordinates to letters
        coordinates = {v: k for k, v in square.items()}
        return square, coordinates

    def encrypt(self, text: str) -> str:
        """
        Encrypts the given plaintext using the Polybius square.

        Args:
            text (str): The plaintext to encrypt.

        Returns:
            str: The encrypted ciphertext.
        """
        text = text.upper().replace(
            "J", "I"
        )  # Replace 'J' with 'I' since they share the same position
        encrypted = ""

        for char in text:
            if char.isalpha():
                try:
                    row, col = self.square[char]
                    encrypted += f"{row}{col}"
                except KeyError:
                    raise ValueError(
                        f"Character '{char}' is not in the Polybius square."
                    )
            else:
                encrypted += char  # Non-alphabetic characters are added as-is

        return encrypted

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the Polybius square.

        Args:
            ciphertext (str): The ciphertext to decrypt.

        Returns:
            str: The decrypted plaintext.
        """
        decrypted = ""
        i = 0

        while i < len(ciphertext):
            if (
                ciphertext[i].isdigit()
                and i + 1 < len(ciphertext)
                and ciphertext[i + 1].isdigit()
            ):
                # Extract the row and column from the ciphertext
                row = int(ciphertext[i])
                col = int(ciphertext[i + 1])

                try:
                    decrypted += self.coordinates[(row, col)]
                except KeyError:
                    raise ValueError(
                        f"Coordinates ({row}, {col}) are not valid in the Polybius square."
                    )
                i += 2
            else:
                # Non-digit characters are added as-is
                decrypted += ciphertext[i]
                i += 1

        return decrypted
