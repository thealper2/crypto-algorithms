class VigenereCipher:
    """
    A class to perform Vigenere cipher encryption and decryption.

    Attributes:
        key (str): The key used for encryption and decryption.
    """

    def __init__(self, key: str):
        """
        Initializes the VigenereCipher with a key.

        Args:
            key (str): The encryption/decryption key.
        """
        if not key or not key.isalpha():
            raise ValueError("Key must be a non-empty alphabetic string.")

        self.key = key.upper()

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using the Vigenere cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")

        encrypted = []
        key_index = 0
        for char in plaintext.upper():
            if char.isalpha():
                p = ord(char) - ord("A")
                k = ord(self.key[key_index]) - ord("A")
                encrypted_char = chr((p + k) % 26 + ord("A"))
                encrypted.append(encrypted_char)
                key_index = (key_index + 1) % len(self.key)
            else:
                encrypted.append(char)

        return "".join(encrypted)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the Vigenere cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        decrypted = []
        key_index = 0
        for char in ciphertext.upper():
            if char.isalpha():
                c = ord(char) - ord("A")
                k = ord(self.key[key_index]) - ord("A")
                decrypted_char = chr((c - k + 26) % 26 + ord("A"))
                decrypted.append(decrypted_char)
                key_index = (key_index + 1) % len(self.key)
            else:
                decrypted.append(char)

        return "".join(decrypted)
