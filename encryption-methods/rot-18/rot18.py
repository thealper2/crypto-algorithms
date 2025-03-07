class ROT18Cipher:
    """
    ROT18 Cipher implementation that rotates both letters and numbers.
    ROT18 is a combination of ROT13 for letters and ROT5 for numbers.
    """

    def __init__(self):
        """
        Initialize the ROT18 Cipher class.
        """
        self.rot13_map = self._create_rot13_mapping()
        self.rot5_map = self._create_rot5_mapping()

    def _create_rot13_mapping(self) -> dict:
        """
        Create a mapping for ROT13 cipher.

        Returns:
            dict: A dictionary containing the ROT13 mapping for upper
        """
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rot13_mapping = {}

        # Create mapping for lowercase letters
        for i, char in enumerate(lowercase):
            rot13_mapping[char] = lowercase[(i + 13) % 26]

        # Create mapping for uppercase letters
        for i, char in enumerate(uppercase):
            rot13_mapping[char] = uppercase[(i + 13) % 26]

        return rot13_mapping

    def _create_rot5_mapping(self) -> dict:
        """
        Create a mapping for ROT5 cipher.

        Returns:
            dict: A dictionary containing the ROT5 mapping for digits.
        """
        digits = "0123456789"
        rot5_mapping = {}

        # Create mapping for digits
        for i, char in enumerate(digits):
            rot5_mapping[char] = digits[(i + 5) % 10]

        return rot5_mapping

    def _rotate_char(self, char: str) -> str:
        """
        Rotate a single character using ROT18 mapping.

        Args:
            char (str): The character to rotate.

        Returns:
            str: The rotated character.

        Raises:
            ValueError: If the character is not a letter or a digit.
        """
        if char in self.rot13_map:
            return self.rot13_map[char]

        elif char in self.rot5_map:
            return self.rot5_map[char]

        else:
            raise ValueError(
                f"Character '{char}' is not a letter or a digit and cannot be rotated."
            )

    def encrypt(self, text: str) -> str:
        """
        Encrypt the input text using ROT18 cipher.

        Args:
            text (str): The text to encrypt.

        Returns:
            str: The encrypted text.
        """
        encrypted_text = []
        for char in text:
            try:
                encrypted_text.append(self._rotate_char(char))

            except ValueError:
                # If the character is not a letter or digit, leave it unchanged
                encrypted_text.append(char)

        return "".join(encrypted_text)

    def decrypt(self, text: str) -> str:
        """
        Decrypt the input text using ROT18 cipher.

        Args:
            text (str): The text to decrypt.

        Returns:
            str: The decrypted text.
        """
        # ROT18 si symmetric, so decryption is the same as encryption.
        return self.encrypt(text)
