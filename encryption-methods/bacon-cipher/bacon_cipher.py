class BaconCipher:
    """
    A class to encode and decode text using the Bacon cipher.

    Attributes:
        bacon_code (Dict[str, str]): A dictionary mapping characters to their 5-bit Bacon codes.
        reverse_bacon_code (Dict[str, str]): A dictionary mapping 5-bit Bacon codes to characters.
    """

    def __init__(self) -> None:
        """
        Initializes the BaconCipher class with the standard Baconian alphabet.
        """
        self.bacon_code = {
            "A": "00000",
            "B": "00001",
            "C": "00010",
            "D": "00011",
            "E": "00100",
            "F": "00101",
            "G": "00110",
            "H": "00111",
            "I": "01000",
            "J": "01000",
            "K": "01001",
            "L": "01010",
            "M": "01011",
            "N": "01100",
            "O": "01101",
            "P": "01110",
            "Q": "01111",
            "R": "10000",
            "S": "10001",
            "T": "10010",
            "U": "10011",
            "V": "10011",
            "W": "10100",
            "X": "10101",
            "Y": "10110",
            "Z": "10111",
        }
        self.reverse_bacon_code = {v: k for k, v in self.bacon_code.items()}

    def encode(self, plaintext: str) -> str:
        """
        Encodes a plaintext message into Bacon cipher binary representation.

        Args:
            plaintext (str): The message to encode.

        Returns:
            str: The encoded binary string.

        Raises:
            ValueError: If the plaintext contains characters not in the Baconian alphabet.
        """
        plaintext = plaintext.upper()
        encoded_message = []

        for char in plaintext:
            if char not in self.bacon_code:
                raise ValueError(f"Character '{char}' is not in the Baconian alphabet.")

            encoded_message.append(self.bacon_code[char])

        return "".join(encoded_message)

    def decode(self, ciphertext: str) -> str:
        """
        Decodes a Bacon cipher binary string into a plaintext message.

        Args:
            ciphertext (str): The binary string to decode.

        Returns:
            str: The decoded plaintext message.

        Raises:
            ValueError: If the ciphertext length is not a multiple of 5 or contains invalid characters.
        """
        if len(ciphertext) % 5 != 0:
            raise ValueError("Ciphertext length must be a multiple of 5.")

        decoded_message = []
        for i in range(0, len(ciphertext), 5):
            binary_chunk = ciphertext[i : i + 5]
            if binary_chunk not in self.reverse_bacon_code:
                raise ValueError(
                    f"Invalid binary chunk '{binary_chunk}' found in ciphertext."
                )

            decoded_message.append(self.reverse_bacon_code[binary_chunk])

        return "".join(decoded_message)
