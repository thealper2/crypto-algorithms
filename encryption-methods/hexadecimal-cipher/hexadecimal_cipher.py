class HexadecimalCipher:
    """
    A class to perform Hexadecimal encoding and decoding operations.
    """

    def __init__(self):
        """
        Initialize the HexadecimalCipher class.
        """
        pass

    def encode(self, text: str) -> str:
        """
        Encode a given text into its hexadecimal representation.

        Args:
            text (str): The input text to encode.

        Returns:
            str: The hexadecimal encoded string.

        Raises:
            ValueError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        hex_string = ""
        for char in text:
            # Convert each character to its hexadecimal representation
            hex_string += hex(ord(char))[2:].zfill(2)

        return hex_string

    def decode(self, hex_string: str) -> str:
        """
        Decode a hexadecimal string back into its original text.

        Args:
            hex_string (str): The hexadecimal string to decode.

        Returns:
            str: The decoded text.

        Raises:
            ValueError: If the input is not a valid hexadecimal string.
        """
        if not isinstance(hex_string, str):
            raise ValueError("Input must be a string.")

        # Ensure the hex string has an even length
        if len(hex_string) % 2 != 0:
            raise ValueError("Invalid hexadecimal string length.")

        text = ""
        try:
            for i in range(0, len(hex_string), 2):
                # Convert each pair of hex digits to a character
                hex_value = hex_string[i : i + 2]
                char = chr(int(hex_value, 16))
                text += char

        except ValueError as e:
            raise ValueError("Invalid hexadecimal string.") from e

        return text
