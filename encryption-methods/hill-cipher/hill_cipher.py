import numpy as np
from typing import Optional


class HillCipher:
    """
    A class to perform Hill Cipher encryption and decryption.

    Attributes:
        key_matrix (np.ndarray): The key matrix used for encryption and decryption.
    """

    def __init__(self, key_matrix: np.ndarray):
        """
        Initialize the HillCipher with a key matrix.

        Args:
            key_matrix (np.ndarray): The key matrix for encryption/decryption.
        """
        self.key_matrix = key_matrix
        self.n = key_matrix.shape[0]

    @staticmethod
    def mod_inverse(a: int, m: int) -> Optional[int]:
        """
        Compute the modular inverse of a under modulo m.

        Args:
            a (int): The number to find the inverse of.
            m (int): The modulo.

        Returns:
            Optional[int]: The modular inverse if it exists, otherwise None.
        """
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using the Hill Cipher method.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        plaintext = plaintext.upper().replace(" ", "")
        if len(plaintext) % self.n != 0:
            plaintext += "X" * (self.n - len(plaintext) % self.n)

        plaintext_numbers = [ord(char) - ord("A") for char in plaintext]
        plaintext_blocks = np.array(plaintext_numbers).reshape(-1, self.n)

        ciphertext = []
        for block in plaintext_blocks:
            encrypted_block = np.dot(self.key_matrix, block) % 26
            ciphertext.extend(encrypted_block)

        return "".join(chr(num + ord("A")) for num in ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the ciphertext using the Hill Cipher method.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If the key matrix is not invertible.
        """
        ciphertext_numbers = [ord(char) - ord("A") for char in ciphertext]
        ciphertext_blocks = np.array(ciphertext_numbers).reshape(-1, self.n)

        det = int(round(np.linalg.det(self.key_matrix)))
        det_inv = self.mod_inverse(det, 26)
        if det_inv is None:
            raise ValueError("Key matrix is not invertible.")

        key_matrix_inv = np.linalg.inv(self.key_matrix) * det
        key_matrix_inv = (key_matrix_inv * det_inv) % 26
        key_matrix_inv = np.round(key_matrix_inv).astype(int) % 26

        plaintext = []
        for block in ciphertext_blocks:
            decrypted_block = np.dot(key_matrix_inv, block) % 26
            plaintext.extend(decrypted_block)

        return "".join(chr(num + ord("A")) for num in plaintext)
