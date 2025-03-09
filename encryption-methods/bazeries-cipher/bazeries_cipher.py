class BazeriesCipher:
    """
    A class to implement the Bazeries cipher.
    """

    def __init__(self, key: int):
        """
        Initialize the Bazeries cipher with a numeric key.

        Args:
            key (int): The numeric key used for the Caesar shift and columnar transposition.
        """
        if not isinstance(key, int) or key <= 0:
            raise ValueError("Key must be a positive integer.")
        self.key = key

    def _caesar_shift(self, text: str, shift: int) -> str:
        """
        Perform a Caesar shift on the input text.

        Args:
            text (str): The text to be shifted.
            shift (int): The number of positions to shift each character.

        Returns:
            str: The shifted text.
        """
        shifted_text = []
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    shifted_char = chr(
                        ((ord(char) - ord("a") + shift_amount) % 26) + ord("a")
                    )
                else:
                    shifted_char = chr(
                        ((ord(char) - ord("A") + shift_amount) % 26) + ord("A")
                    )
                shifted_text.append(shifted_char)
            else:
                shifted_text.append(char)
        return "".join(shifted_text)

    def _columnar_transposition(self, text: str, key: int) -> str:
        """
        Perform a columnar transposition on the input text using the numeric key.

        Args:
            text (str): The text to be transposed.
            key (int): The numeric key used to determine the column order.

        Returns:
            str: The transposed text.
        """
        key_str = str(key)
        key_length = len(key_str)
        text_length = len(text)

        # Pad the text if necessary
        if text_length % key_length != 0:
            padding_length = key_length - (text_length % key_length)
            text += " " * padding_length

        # Arrange text in rows
        rows = [text[i : i + key_length] for i in range(0, len(text), key_length)]

        # Sort columns based on the key
        sorted_columns = sorted(range(key_length), key=lambda x: key_str[x])

        # Read columns in sorted order
        transposed_text = []
        for col in sorted_columns:
            for row in rows:
                transposed_text.append(row[col])
        return "".join(transposed_text)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using the Bazeries cipher.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")

        # Step 1: Apply Caesar shift using the key
        shifted_text = self._caesar_shift(plaintext, self.key)

        # Step 2: Apply columnar transposition using the key
        encrypted_text = self._columnar_transposition(shifted_text, self.key)

        return encrypted_text

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the ciphertext using the Bazeries cipher.

        Args:
            ciphertext (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        # Step 1: Reverse the columnar transposition
        key_str = str(self.key)
        key_length = len(key_str)
        text_length = len(ciphertext)

        # Determine the number of rows
        num_rows = text_length // key_length

        # Sort columns based on the key
        sorted_columns = sorted(range(key_length), key=lambda x: key_str[x])

        # Reconstruct the transposed text
        transposed_text = [""] * text_length
        index = 0
        for col in sorted_columns:
            for row in range(num_rows):
                transposed_text[row * key_length + col] = ciphertext[index]
                index += 1

        transposed_text = "".join(transposed_text)

        # Step 2: Reverse the Caesar shift
        decrypted_text = self._caesar_shift(transposed_text, -self.key)

        return decrypted_text.strip()
