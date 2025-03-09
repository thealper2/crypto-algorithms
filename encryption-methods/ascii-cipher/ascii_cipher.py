class ASCIICipher:
    """
    A class to implement the ASCII cipher.
    """

    def __init__(self, shift: int):
        """
        Initialize the ASCIICipher with a shift value.

        Args:
            shift (int): The number of positions to shift each character in the string.
        """
        self.shift = shift

    def encrypt(self, text: str) -> str:
        """
        Encrypt the input text by shifting each character's ASCII value.

        Args:
            text (str): The input string to encrypt.

        Returns:
            str: The encrypted string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        encrypted_text = []
        for char in text:
            # Shift the ASCII value and wrap around if necessary
            shifted_char = chr((ord(char) + self.shift) % 128)
            encrypted_text.append(shifted_char)

        return "".join(encrypted_text)

    def decrypt(self, text: str) -> str:
        """
        Decrypt the input text by shifting each character's ASCII value in the opposite function.

        Args:
            text (str): The input string to decrypt.

        Returns:
            str: The decrypted string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        decrypted_text = []
        for char in text:
            # Shift the ASCII value back and wrap around if necessary
            shifted_char = chr((ord(char) - self.shift) % 128)
            decrypted_text.append(shifted_char)

        return "".join(decrypted_text)
