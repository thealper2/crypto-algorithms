import math


class RowColumnCipher:
    """
    A class to perform row-column transposition encryption and decryption.

    Attributes:
        plaintext (str): The text to be encrypted or decrypted.
        num_cols (int): The number of columns used in the transposition cipher.
    """

    def __init__(self, plaintext: str, num_cols: int):
        """
        Initializes the RowColumnCipher with the provided plaintext and number of columns.

        Args:
            plaintext (str): The text to be encrypted or decrypted.
            num_cols (int): The number of columns used in the transposition cipher.
        """
        self.plaintext = plaintext
        self.num_cols = num_cols

    def encrypt(self) -> str:
        """
        Encrypts the plaintext using row-column transposition.

        Returns:
            str: The encrypted ciphertext.
        """
        try:
            num_rows = math.ceil(len(self.plaintext) / self.num_cols)
            padded_length = num_rows * self.num_cols
            padded_plaintext = self.plaintext.ljust(padded_length, "X")

            ciphertext = ""
            for col in range(self.num_cols):
                for row in range(num_rows):
                    idx = row * self.num_cols + col
                    ciphertext += padded_plaintext[idx]

            return ciphertext
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {e}")

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using row-column transposition.

        Args:
            ciphertext (str): The encrypted text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        try:
            num_rows = math.ceil(len(ciphertext) / self.num_cols)
            plaintext = [""] * len(ciphertext)
            idx = 0

            for col in range(self.num_cols):
                for row in range(num_rows):
                    if idx < len(ciphertext):
                        plaintext[row * self.num_cols + col] = ciphertext[idx]
                        idx += 1

            return "".join(plaintext).rstrip("X")
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {e}")
