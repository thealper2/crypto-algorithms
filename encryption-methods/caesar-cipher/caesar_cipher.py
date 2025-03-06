from typing import Optional


class CaesarCipher:
    """
    A class to perform Caesar cipher encryption and decryption.

    Attributes:
        shift (int): The number of positions to shift the characters.
    """

    def __init__(self, shift: int = 3):
        """
        Initializes the CaesarCipher with a specified shift value.

        Args:
            shift (int): The number of positions to shift the characters. Default is 3.
        """
        self.shift = shift

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using the Caesar cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        encrypted = ""
        for char in plaintext:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                encrypted += chr((ord(char) - base + self.shift) % 26 + base)

            else:
                encrypted += char

        return encrypted

    def decrypt(self, ciphertext: str, shift: Optional[int] = None) -> str:
        """
        Decrypts the given plaintext using the Caesar cipher.

        If no shift value is provided, a brute-force approach is used to try all possible shifts.

        Args:
            ciphertext (str): The text to be decrypted.
            shift (Optional[int]): The number of positions to shift the characters. If None, brute-force is used.

        Returns:
            str: The decrypted text.
        """
        if shift is not None:
            return self._decrypt_with_shift(ciphertext, shift)
        else:
            return self._brute_force_decrypt(ciphertext)

    def _decrypt_with_shift(self, ciphertext: str, shift: int) -> str:
        """
        Decrypts the ciphertext using a specified shift value.

        Args:
            ciphertext (str): The text to be decrypted.
            shift (int): The number of positions to shift the characters.

        Returns:
            str: The decrypted text.
        """
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                decrypted += chr((ord(char) - base - shift) % 26 + base)

            else:
                decrypted += char

        return decrypted

    def _brute_force_decrypt(self, ciphertext: str) -> str:
        """
        Attempts to decrypt the ciphertext by trying all possible shift values.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        print(
            "* Brute force decryption attempted. Check output for possible solutions."
        )
        for possible_shift in range(26):
            decrypted = self._decrypt_with_shift(ciphertext, possible_shift)
            print(f"Shift {possible_shift}: {decrypted}")
