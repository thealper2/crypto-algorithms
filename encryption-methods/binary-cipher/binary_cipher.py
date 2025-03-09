class BinaryCipher:
    """
    A class to encode and decode text using binary representation.

    Attributes:
        None
    """

    @staticmethod
    def _validate_input(text: str) -> None:
        """
        Validates the input text to ensure it is not empty.

        Args:
            text (str): The input text to validate.

        Raises:
            ValueError: If the input text is empty.
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

    @staticmethod
    def _text_to_binary(text: str) -> str:
        """
        Converts a given text to its binary representation.

        Args:
            text (str): The text to convert to binary.

        Returns:
            str: The binary representation of the text.
        """
        return " ".join(format(ord(char), "08b") for char in text)

    @staticmethod
    def _binary_to_text(binary: str) -> str:
        """
        Converts a given binary string back to text.

        Args:
            binary (str): The binary string to convert to text.

        Returns:
            str: The decoded text.
        """
        return "".join(chr(int(b, 2)) for b in binary.split())

    def encode(self, text: str) -> str:
        """
        Encodes the given text into binary.

        Args:
            text (str): The text to encode.

        Returns:
            str: The binary-encoded text.

        Raises:
            ValueError: If the input text is empty.
        """
        self._validate_input(text)
        return self._text_to_binary(text)

    def decode(self, binary: str) -> str:
        """
        Decodes the given binary string back to text.

        Args:
            binary (str): The binary string to decode.

        Returns:
            str: The decoded text.

        Raises:
            ValueError: If the input binary string is empty or invalid.
        """
        self._validate_input(binary)
        try:
            return self._binary_to_text(binary)
        except ValueError:
            raise ValueError("Invalid binary input. Ensure it is properly formatted.")
