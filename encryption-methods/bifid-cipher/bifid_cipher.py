from typing import List, Tuple, Dict, Set


class BifidCipher:
    """
    A class to handle the Bifid cipher encryption and decryption using a Polybius square.
    """

    def __init__(self, key: str):
        """
        Initializes the BifidCipher with a specific key to generate the Polybius square.

        Args:
            key (str): The key used to generate the Polybius square. It should be a string.
        """
        self.key = key.upper().replace("J", "I")
        self.square, self.positions = self._create_polybius_square()

    def _create_polybius_square(
        self,
    ) -> Tuple[List[List[str]], Dict[str, Tuple[int, int]]]:
        """
        Creates a Polybius square based on the key provided during initialization.

        Returns:
            Tuple[List[List[str]], Dict[str, Tuple[int, int]]]: A tuple containing the Polybius square (5x5 grid) and a dictionary mapping characters to their positions.
        """
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_square = []
        used_chars: Set[str] = set()

        # Add characters from the key to the square, avoiding duplicates
        for char in self.key:
            if char not in used_chars and char in alphabet:
                key_square.append(char)
                used_chars.add(char)

        # Fill the rest of the square with the remaining alphabet letters
        for char in alphabet:
            if char not in used_chars:
                key_square.append(char)

        # Organize the square into a 5x5 grid
        square = [key_square[i : i + 5] for i in range(0, 25, 5)]
        positions = {char: (i // 5, i % 5) for i, char in enumerate(key_square)}
        return square, positions

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Bifid cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        plaintext = plaintext.upper().replace("J", "I")
        row_coords = []
        col_coords = []

        # Collect row and column coordinates for each character in the plaintext
        for char in plaintext:
            if char in self.positions:
                row, col = self.positions[char]
                row_coords.append(row)
                col_coords.append(col)
            else:
                raise ValueError(f"Character {char} not found in Polybius square.")

        # Combine row and column coordinates and form the ciphertext
        combined_coords = row_coords + col_coords
        ciphertext = ""
        for i in range(0, len(combined_coords), 2):
            row = combined_coords[i]
            col = combined_coords[i + 1]
            ciphertext += self.square[row][col]

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using the Bifid cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        coords = []

        # Collect all coordinates from the ciphertext
        for char in ciphertext:
            if char in self.positions:
                coords.extend(self.positions[char])
            else:
                raise ValueError(f"Character {char} not found in Polybius square.")

        # Split coordinates into row and column parts
        row_coords = coords[: len(coords) // 2]
        col_coords = coords[len(coords) // 2 :]

        # Reconstruct the plaintext from the coordinates
        plaintext = ""
        for r, c in zip(row_coords, col_coords):
            plaintext += self.square[r][c]

        return plaintext
