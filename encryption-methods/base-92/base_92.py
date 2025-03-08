class Base92Cipher:
    """
    A class to encode and decode data using the Base92 algorithm.

        Attributes:
        BASE92_CHARS (str): The character set used for Base92 encoding.
    """

    BASE92_CHARS = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    def __init__(self):
        """
        Initializes the Base92 encoder/decoder.
        """
        pass

    def encode(self, data: bytes) -> str:
        """
        Encodes the given bytes into a Base92 string.

        Args:
            data (bytes): The binary data to encode.

        Returns:
            str: The Base92 encoded string.

        Raises:
            TypeError: If the input is not of type bytes.
        """
        if not isinstance(data, bytes):
            raise TypeError("Input must be of type bytes.")

        bit_string = "".join(f"{byte:08b}" for byte in data)
        bit_length = len(bit_string)
        encoded_string = ""
        value = 0

        for i in range(0, bit_length, 13):
            chunk = bit_string[i : i + 13]
            value = int(chunk, 2)
            encoded_string += self.BASE92_CHARS[value % 92]
            if value >= 92:
                encoded_string += self.BASE92_CHARS[value // 92]

        return encoded_string

    def decode(self, encoded_string: str) -> bytes:
        """
        Decodes the given Base92 string into bytes.

        Args:
            encoded_string (str): The Base92 encoded string.

        Returns:
            bytes: The decoded binary data.

        Raises:
            TypeError: If the input is not of type str.
            ValueError: If the input contains invalid Base92 characters.
        """
        if not isinstance(encoded_string, str):
            raise TypeError("Input must be of type str.")

        if any(char not in self.BASE92_CHARS for char in encoded_string):
            raise ValueError("Input contains invalid Base92 characters.")

        bit_string = ""
        value = 0

        for char in encoded_string:
            char_value = self.BASE92_CHARS.index(char)
            value = value * 92 + char_value
            if value > 0xFFFF:
                bit_string += f"{(value >> 8):08b}"
                value &= 0xFF

        if value:
            bit_string += f"{value:08b}"

        # Pad the bit string to make its length a multiple of 8
        padding = len(bit_string) % 8
        if padding:
            bit_string = bit_string[:-padding]

        # Convert the bit string to bytes
        byte_array = bytearray()
        for i in range(0, len(bit_string), 8):
            byte = bit_string[i : i + 8]
            byte_array.append(int(byte, 2))

        return bytes(byte_array)
