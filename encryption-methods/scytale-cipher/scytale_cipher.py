class ScytaleCipher:
    """
    A class to implement the Scytale cipher encryption and decryption.

    Attributes:
        key (int): The number of rows used in the Scytale cipher.
    """

    def __init__(self, key: int):
        """
        Initializes the ScytaleCipher with a specific key.

        Args:
            key (int): The number of rows to use in the cipher.

        Raises:
            ValueError: If the key is less than or equal to 0.
        """
        if key <= 0:
            raise ValueError("Key must be a positive integer.")

        self.key = key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Scytale cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """

        # Remove any spaces and convert to uppercase
        plaintext = plaintext.replace(" ", "").upper()
        ciphertext = []

        # Calculate the number of columns needed
        columns = (len(plaintext) + self.key - 1) // self.key

        # Write the plaintext in rows and read columns to get ciphertext
        for col in range(columns):
            for row in range(self.key):
                index = row * columns + col
                if index < len(plaintext):
                    ciphertext.append(plaintext[index])
                else:
                    ciphertext.append("")  # Padding if necessary

        return "".join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using the Scytale cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """

        plaintext = []

        # Calculate the number of columns used during encryption.
        columns = (len(ciphertext) + self.key - 1) // self.key

        # Read the ciphertext in columns and write rows to get plaintext
        for row in range(self.key):
            for col in range(columns):
                index = col * self.key + row
                if index < len(ciphertext):
                    plaintext.append(ciphertext[index])

        return "".join(plaintext)
