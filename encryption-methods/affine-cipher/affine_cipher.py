import math
from typing import Optional


class AffineCipher:
    """
    A class to handle Affine cipher encryption and decryption.
    """

    def __init__(self, a: int = 5, b: int = 8):
        """
        Initialize the AffineCipher with keys a and b.

        Args:
            a (int): The multiplicative key. Must be coprime with 26.
            b (int): The additive key.
        """
        if math.gcd(a, 26) != 1:
            raise ValueError("Key 'a' must be coprime with 26.")

        self.a = a
        self.b = b

    @staticmethod
    def mod_inverse(a: int, m: int) -> Optional[int]:
        """
        Calculate the modular inverse of a under modulo m.

        Args:
            a (int): The number to find the inverse of.
            m (int): The modulo.

        Returns:
            Optional[int]: The modular inverse if it exists, otherwise None.
        """
        for x in range(1, m):
            if (a * x) % m == 1:
                return x

        return None

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using the Affine Cipher.

        Args:
            plaintext (str): The text to encrypt.

        Returns:
            str: The encrypted ciphertext.
        """
        encrypted = ""
        for char in plaintext.upper():
            if char.isalpha():
                x = ord(char) - ord("A")
                encrypted += chr(((self.a * x + self.b) % 26) + ord("A"))
            else:
                encrypted += char

        return encrypted

    def decrypt(self, ciphertext: str, a: int = 5, b: int = 8) -> str:
        """
        Decrypt the ciphertext using the Affine Cipher.

        Args:
            ciphertext (str): The text to decrypt.
            a (int): The multiplicative key.
            b (int): The additive key.

        Returns:
            str: The decrypted plaintext.
        """
        if math.gcd(a, 26) != 1:
            raise ValueError("Key 'a' must be coprime with 26.")

        a_inv = self.mod_inverse(a, 26)
        if a_inv is None:
            raise ValueError("No modular inverse exists for the given key 'a'.")

        decrypted = ""
        for char in ciphertext.upper():
            if char.isalpha():
                y = ord(char) - ord("A")
                decrypted += chr(((a_inv * (y - b)) % 26) + ord("A"))

            else:
                decrypted += char

        return decrypted
