from typing import Union


class Base64Cipher:
    """
    A class to encode and decode data using the Base64 algorithm.
    """

    # Base64 character set
    _BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def __init__(self):
        """
        Initializes the Base64Cipher class.
        """
        # Create a dictionary to map characters to their Base64 index for faster decoding
        self._char_to_index = {char: idx for idx, char in enumerate(self._BASE64_CHARS)}

    def encode(self, data: Union[str, bytes]) -> str:
        """
        Encodes the input data into Base64.

        Args:
            data (Union[str, bytes]): The data to encode. Can be a string or bytes.

        Returns:
            str: The Base64 encoded string.

        Raises:
            TypeError: If the input data is not a string or bytes.
        """
        if isinstance(data, str):
            data = data.encode("utf-8")  # Convert string to bytes
        elif not isinstance(data, bytes):
            raise TypeError("Input data must be a string or bytes.")

        encoded = []
        padding_length = 0

        # Process the input in chunks of 3 bytes
        for i in range(0, len(data), 3):
            chunk = data[i : i + 3]
            padding_length = 3 - len(chunk)

            # Pad the chunk if necessary
            chunk += b"\x00" * padding_length

            # Combine the 3 bytes into a 24-bit integer
            combined = int.from_bytes(chunk, "big")

            # Split the 24-bit integer into four 6-bit indices
            for j in range(3, -1, -1):
                index = (combined >> (6 * j)) & 0x3F
                encoded.append(self._BASE64_CHARS[index])

        # Replace padding characters with '='
        if padding_length > 0:
            encoded[-padding_length:] = ["="] * padding_length

        return "".join(encoded)

    def decode(self, encoded_data: str) -> bytes:
        """
        Decodes a Base64 encoded string back into bytes.

        Args:
            encoded_data (str): The Base64 encoded string.

        Returns:
            bytes: The decoded bytes.

        Raises:
            ValueError: If the input is not a valid Base64 string.
        """
        if len(encoded_data) % 4 != 0:
            raise ValueError("Invalid Base64 input: length must be multiple of 4.")

        # Remove padding characters and calculate padding length
        encoded_data = encoded_data.rstrip("=")

        decoded = bytearray()
        combined = 0
        bits_collected = 0

        for char in encoded_data:
            if char not in self._char_to_index:
                raise ValueError(f"Invalid character in Base64 input: {char}")

            # Combine the 6-bit indices into a 24-bit integer
            combined = (combined << 6) | self._char_to_index[char]
            bits_collected += 6

            # When 24 bits are collected, extract 3 bytes
            if bits_collected >= 8:
                bits_collected -= 8
                decoded.append((combined >> bits_collected) & 0xFF)

        return bytes(decoded)
