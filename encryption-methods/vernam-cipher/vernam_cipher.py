class VernamCipher:
    """
    A class to perform encryption and decryption using the Vernam Cipher (One-Time Pad) algorithm.
    The Vernam Cipher is a symmetric key algorithm where the plaintext is XORed with a key to produce ciphertext.
    The key must be of the same length as the plaintext for the algorithm to work correctly.
    """

    def __init__(self):
        pass

    def _text_to_binary(self, text: str) -> str:
        """
        Converts a given text to its binary representation.

        Args:
            text (str): The input text to convert.

        Returns:
            str: Binary representation of the input text.
        """
        return "".join(format(ord(char), "08b") for char in text)

    def _binary_to_text(self, binary: str) -> str:
        """
        Converts a binary string to its text representation.

        Args:
            binary (str): The binary string to convert.

        Returns:
            str: Text representation of the binary string.
        """
        chars = [binary[i : i + 8] for i in range(0, len(binary), 8)]
        return "".join(chr(int(char, 2)) for char in chars)

    def encrypt(self, plaintext: str, key: str) -> str:
        """
        Encrypts the plaintext using the Vernam Cipher algorithm.

        Args:
            plaintext (str): The plaintext to encrypt.
            key (str): The key used for encryption. Must be the same length as the plaintext.

        Returns:
            str: The encrypted ciphertext in binary format.

        Raises:
            ValueError: If the length of the plaintext and key do not match.
        """
        binary_plaintext = self._text_to_binary(plaintext)
        binary_key = self._text_to_binary(key)

        if len(binary_plaintext) != len(binary_key):
            raise ValueError("Plaintext and key must be of the same length.")

        ciphertext = "".join(
            "1" if p != k else "0" for p, k in zip(binary_plaintext, binary_key)
        )
        return ciphertext

    def decrypt(self, ciphertext: str, key: str) -> str:
        """
        Decrypts the ciphertext using the Vernam Cipher algorithm.

        Args:
            ciphertext (str): The ciphertext to decrypt (in binary format).
            key (str): The key used for decryption. Must be the same length as the ciphertext.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If the length of the ciphertext and key do not match.
        """
        binary_key = self._text_to_binary(key)

        if len(ciphertext) != len(binary_key):
            raise ValueError("Ciphertext and key must be of the same length.")

        plaintext_binary = "".join(
            "1" if c != k else "0" for c, k in zip(ciphertext, binary_key)
        )
        return self._binary_to_text(plaintext_binary)
