class AtbashCipher:
    """
    A lcass to perform Atbash cipher encryption and decryption.
    """

    def __init__(self):
        """
        Initialize the AtbashCipher class.
        """
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.reversed_alphabet = self.alphabet[::-1]

    def _validate_input(self, text: str) -> str:
        """
        Validate the input text to ensure it contains only alphabetic characters.

        Args:
            text (str): The input text to be validated.

        Returns:
            str: The validated text in uppercase.

        Raises:
            ValueError: If the input text contains non-alphabetic characters.
        """
        if not text.isalpha():
            raise ValueError("Input text must contain only alphabetic characters.")

        return text.upper()

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the given plaintext using the Atbash cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        plaintext = self._validate_input(plaintext)
        ciphertext = []
        for char in plaintext:
            index = self.alphabet.index(char)
            ciphertext.append(self.reversed_alphabet[index])

        return "".join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the given ciphertext using the Atbash cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        ciphertext = self._validate_input(ciphertext)
        plaintext = []
        for char in ciphertext:
            index = self.reversed_alphabet.index(char)
            plaintext.append(self.alphabet[index])

        return "".join(plaintext)
