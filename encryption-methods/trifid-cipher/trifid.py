from typing import Optional, Tuple


class TrifidCipher:
    """
    A class to implement the Trifid cipher encryption and decryption.

    The Trifid cipher uses a 3x3x3 cube to map letters to coordinates and vice versa.
    It is a more complex cipher compared to the Bifid cipher, offering enhanced security.

    Attributes:
        cube (List[List[List[str]]]): A 3D cube representing the Trifid cipher's alphabet.
        layer_size (int): The size of each layer in the cube (3x3).
    """

    def __init__(self) -> None:
        """
        Initializes the TrifidCipher class with a predefined 3x3x3 cube.
        """
        self.cube = [
            [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
            [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
            [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "_"]],
        ]
        self.layer_size = 3

    def _find_position(self, char: str) -> Optional[Tuple[int, int, int]]:
        """
        Finds the position (layer, row, column) of a character in the cube.

        Args:
            char (str): The character to find in the cube.

        Returns:
            Optional[Tuple[int, int, int]]: A tuple containing (layer, row, column) indices.
                                            Returns None if the character is not found.
        """
        for layer in range(self.layer_size):
            for row in range(self.layer_size):
                for col in range(self.layer_size):
                    if self.cube[layer][row][col] == char:
                        return (layer, row, col)
        return None

    def _get_character(self, layer: int, row: int, col: int) -> str:
        """
        Retrieves the character at a specific position in the cube.

        Args:
            layer (int): The layer index.
            row (int): The row index.
            col (int): The column index.

        Returns:
            str: The character at the specified position.

        Raises:
            ValueError: If the indices are out of bounds.
        """
        if not (
            0 <= layer < self.layer_size
            and 0 <= row < self.layer_size
            and 0 <= col < self.layer_size
        ):
            raise ValueError("Indices are out of bounds for the cube.")
        return self.cube[layer][row][col]

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using the Trifid cipher.

        Args:
            plaintext (str): The text to encrypt.

        Returns:
            str: The encrypted ciphertext.

        Raises:
            ValueError: If the plaintext contains characters not in the cube.
        """
        # Convert plaintext to uppercase and remove spaces
        plaintext = plaintext.upper().replace(" ", "")
        coordinates = []

        # Get coordinates for each character
        for char in plaintext:
            pos = self._find_position(char)
            if pos is None:
                raise ValueError(f"Character '{char}' is not in the cube.")
            coordinates.extend(pos)

        # Split coordinates into three streams
        layer_stream = coordinates[::3]
        row_stream = coordinates[1::3]
        col_stream = coordinates[2::3]

        # Combine streams and split into triplets
        combined_stream = layer_stream + row_stream + col_stream
        triplets = [
            combined_stream[i : i + 3] for i in range(0, len(combined_stream), 3)
        ]

        # Convert triplets back to characters
        ciphertext = ""
        for triplet in triplets:
            if len(triplet) == 3:
                ciphertext += self._get_character(triplet[0], triplet[1], triplet[2])
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the Trifid cipher.

        Args:
            ciphertext (str): The text to decrypt.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If the ciphertext contains characters not in the cube.
        """
        # Convert ciphertext to uppercase and remove spaces
        ciphertext = ciphertext.upper().replace(" ", "")
        coordinates = []

        # Get coordinates for each character
        for char in ciphertext:
            pos = self._find_position(char)
            if pos is None:
                raise ValueError(f"Character '{char}' is not in the cube.")
            coordinates.extend(pos)

        # Split coordinates into three streams
        combined_stream = coordinates
        stream_length = len(combined_stream) // 3
        layer_stream = combined_stream[:stream_length]
        row_stream = combined_stream[stream_length : 2 * stream_length]
        col_stream = combined_stream[2 * stream_length :]

        # Reconstruct original coordinates
        original_coordinates = []
        for i in range(stream_length):
            original_coordinates.append(layer_stream[i])
            original_coordinates.append(row_stream[i])
            original_coordinates.append(col_stream[i])

        # Convert coordinates back to characters
        plaintext = ""
        for i in range(0, len(original_coordinates), 3):
            if i + 2 < len(original_coordinates):
                plaintext += self._get_character(
                    original_coordinates[i],
                    original_coordinates[i + 1],
                    original_coordinates[i + 2],
                )
        return plaintext
