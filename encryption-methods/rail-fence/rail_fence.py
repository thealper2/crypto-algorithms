from typing import List


class RailFenceCipher:
    """
    A class to perform Rail Fence Cipher encryption and decryption.

    Attributes:
        num_rails (int): The number of rails to use for the cipher.
    """

    def __init__(self, num_rails: int):
        """
        Initializes the RailFenceCipher with the specified number of rails.

        Args:
            num_rails (int): The number of rails to use for the cipher.

        Raises:
            ValueError: If the number of rails is less than 2.
        """
        if num_rails < 2:
            raise ValueError("Number of rails must be at least 2.")
        self.num_rails = num_rails

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using the Rail Fence Cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        rails: List[str] = ["" for _ in range(self.num_rails)]
        rail: int = 0
        direction: int = 1  # 1: Down, -1: Up

        for char in plaintext:
            rails[rail] += char
            rail += direction
            if rail == 0 or rail == self.num_rails - 1:
                direction *= -1

        return "".join(rails)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the Rail Fence Cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        rail_lengths: List[int] = [0] * self.num_rails
        rail: int = 0
        direction: int = 1

        for _ in ciphertext:
            rail_lengths[rail] += 1
            rail += direction
            if rail == 0 or rail == self.num_rails - 1:
                direction *= -1

        rails: List[List[str]] = []
        idx: int = 0
        for length in rail_lengths:
            rails.append(list(ciphertext[idx : idx + length]))
            idx += length

        result: List[str] = []
        rail: int = 0
        direction: int = 1

        for _ in ciphertext:
            result.append(rails[rail].pop(0))
            rail += direction
            if rail == 0 or rail == self.num_rails - 1:
                direction *= -1

        return "".join(result)
