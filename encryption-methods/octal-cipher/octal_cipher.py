class OctalCipher:
    """
    A class to implement the Octal Cipher.
    """

    def __init__(self):
        """
        Initialize the OctalCipher class.
        """
        pass

    def encode(self, text: str) -> str:
        """
        Convert a given text to its octal representation.

        Args:
            text (str): The input text to be converted.

        Returns:
            str: The octal representation of the input text.

        Raises:
            ValueError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        octal_result = []
        for char in text:
            # Convert each character to its ASCII value, then to its octal representation
            octal_value = oct(ord(char))[2:]  # Remove the '0o' prefix
            octal_result.append(octal_value)

        return " ".join(octal_result)

    def decode(self, octal_str: str) -> str:
        """
        Convert a given octal string back to its original text.

        Args:
            octal_str (str): The octal string to be converted.

        Returns:
            str: The original text.

        Raises:
            ValueError: If the input is not a valid octal string.
        """
        if not isinstance(octal_str, str):
            raise ValueError("Input must be a string.")

        try:
            octal_values = octal_str.split()
            text_result = []
            for octal_value in octal_values:
                # Convert each octal value to its corresponding character
                char = chr(int(octal_value, 8))
                text_result.append(char)

            return "".join(text_result)

        except ValueError as e:
            raise ValueError("Invalid octal string provided.") from e
