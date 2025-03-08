class Base32Cipher:
    """
    A class to encode and decode data using the Base32 algorithm.
    """

    # Base32 character set (RFC 4648)
    BASE32_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    PADDING_CHAR = "="

    def __init__(self):
        """
        Initialize the Base32Cipher class.
        """
        # Create a mapping from characters to their Base32 index for fast lookup
        self.char_to_index = {char: idx for idx, char in enumerate(self.BASE32_CHARS)}

    def encode(self, data: bytes) -> str:
        """
        Encode the given bytes into a Base32 string.

        Args:
            data (bytes): The input data to encode.

        Returns:
            str: The Base32-encoded string.

        Raises:
            ValueError: If the input data is empty.
        """
        if not data:
            raise ValueError("Input data cannot be empty.")

        encoded = []
        buffer = 0
        buffer_length = 0

        for byte in data:
            # Shift the buffer left by 8 bits and add the current byte
            buffer = (buffer << 8) | byte
            buffer_length += 8

            # Extract 5-bit chunks from the buffer
            while buffer_length >= 5:
                # Extract the top 5 bits
                index = (buffer >> (buffer_length - 5)) & 0x1F
                encoded.append(self.BASE32_CHARS[index])
                buffer_length -= 5
                buffer &= (1 << buffer_length) - 1  # Clear the processed bits

        # Handle any remaining bits in the buffer
        if buffer_length > 0:
            # Pad the remaining bits to form a 5-bit chunk
            index = (buffer << (5 - buffer_length)) & 0x1F
            encoded.append(self.BASE32_CHARS[index])

        # Add padding characters if necessary
        padding_length = (8 - len(encoded)) % 8
        if padding_length != 8:
            encoded.extend([self.PADDING_CHAR] * padding_length)

        return "".join(encoded)

    def decode(self, encoded: str) -> bytes:
        """
        Decode the given Base32 string into bytes.

        Args:
            encoded (str): The Base32-encoded string.

        Returns:
            bytes: The decoded data.

        Raises:
            ValueError: If the input string is empty or contains invalid characters.
        """
        if not encoded:
            raise ValueError("Input string cannot be empty.")

        # Remove padding characters and convert to uppercase
        encoded = encoded.rstrip(self.PADDING_CHAR).upper()

        decoded = []
        buffer = 0
        buffer_length = 0

        for char in encoded:
            if char not in self.char_to_index:
                raise ValueError(f"Invalid character in input: {char}")

            # Add the 5-bit chunk to the buffer
            buffer = (buffer << 5) | self.char_to_index[char]
            buffer_length += 5

            # Extract 8-bit chunks from the buffer
            while buffer_length >= 8:
                # Extract the top 8 bits
                byte = (buffer >> (buffer_length - 8)) & 0xFF
                decoded.append(byte)
                buffer_length -= 8
                buffer &= (1 << buffer_length) - 1  # Clear the processed bits

        return bytes(decoded)
