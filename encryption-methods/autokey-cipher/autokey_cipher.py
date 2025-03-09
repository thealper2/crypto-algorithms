class AutokeyCipher:
    """
    A class to implement the Autokey Cipher encryption and decryption.

    Attributes:
        key (str): The keyword used for encryption and decryption.
    """

    def __init__(self, key: str):
        """
        Initializes the AutokeyCipher with a given key.

        Args:
            key (str): The keyword to be used for encryption and decryption.
        """
        if not key.isalpha():
            raise ValueError("Key must contain only alphabetic characters.")

        self.key = key.upper()

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using the Autokey Cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        if not plaintext.isalpha():
            raise ValueError("Plaintext must contain only alphabetic characters.")

        plaintext = plaintext.upper()
        ciphertext = []
        key_stream = self.key + plaintext  # Autokey: Key + Plaintext

        for i, char in enumerate(plaintext):
            if char == " ":
                ciphertext.append(" ")
                continue

            # Calculate the shift for the current character
            shift = ord(key_stream[i]) - ord("A")
            encrypted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            ciphertext.append(encrypted_char)

        return "".join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the Autokey Cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        if not ciphertext.isalpha():
            raise ValueError("Ciphertext must contain only alphabetic characters.")

        ciphertext = ciphertext.upper()
        plaintext = []
        key_stream = self.key  # Start with the initial key

        for i, char in enumerate(ciphertext):
            if char == " ":
                plaintext.append(" ")
                continue

            # Calculate the shift for the current character
            shift = ord(key_stream[i]) - ord("A")
            decrypted_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            plaintext.append(decrypted_char)

            # Update the key stream with the decrypted character
            key_stream += decrypted_char

        return "".join(plaintext)
