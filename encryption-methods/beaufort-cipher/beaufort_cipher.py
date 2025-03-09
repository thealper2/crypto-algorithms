class BeaufortCipher:
    """
    A class to implement the Beaufort cipher encryption and decryption.
    """

    def __init__(self, key: str) -> None:
        """
        Initializes the cipher with a given key.

        Args:
            key (str): The keyword used for encryption and decryption.
        """
        if not key.isalpha():
            raise ValueError("Key must only contain alphabetic characters.")
        self.key = key.upper()

    def _process(self, text: str) -> str:
        """
        Encrypts or decrypts a given text using the Beaufort cipher.

        Args:
            text (str): The text to encrypt or decrypt.

        Returns:
            str: The processed (encrypted/decrypted) text.
        """
        if not text.isalpha():
            raise ValueError("Text must only contain alphabetic characters.")

        text = text.upper()
        key_length = len(self.key)
        result = []

        for i, char in enumerate(text):
            key_char = self.key[i % key_length]
            char_code = ord(char) - 65
            key_code = ord(key_char) - 65
            new_char = chr((key_code - char_code) % 26 + 65)
            result.append(new_char)

        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Beaufort cipher.

        Args:
            plaintext (str): The plaintext to encrypt.

        Returns:
            str: The encrypted text.
        """
        return self._process(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using the Beaufort cipher.

        Args:
            ciphertext (str): The ciphertext to decrypt.

        Returns:
            str: The decrypted text.
        """
        return self._process(ciphertext)
