class Base45Cipher:
    """
    A class to encode and decode data using Base45 encoding.
    """

    ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
    BASE = 45

    @classmethod
    def encode(cls, data: bytes) -> str:
        """
        Encodes a given bytes-like object into a Base45 string.

        Args:
            data (bytes): The input bytes to encode.

        Returns:
            str: A Base45 encoded string.
        """
        encoded_str = ""
        length = len(data)
        i = 0

        while i < length:
            if i + 1 < length:
                # Process two bytes at a time
                value = (data[i] << 8) + data[i + 1]
                encoded_str += cls.ALPHABET[value % cls.BASE]
                encoded_str += cls.ALPHABET[(value // cls.BASE) % cls.BASE]
                encoded_str += cls.ALPHABET[value // (cls.BASE * cls.BASE)]
                i += 2
            else:
                # Process the last byte
                value = data[i]
                encoded_str += cls.ALPHABET[value % cls.BASE]
                encoded_str += cls.ALPHABET[value // cls.BASE]
                i += 1

        return encoded_str

    @classmethod
    def decode(cls, encoded: str) -> bytes:
        """
        Decodes a given Base45 string into its original byte representation.

        Args:
            encoded (str): The Base45 encoded string.

        Returns:
            bytes: The decoded bytes.
        """
        decoded_bytes = bytearray()
        length = len(encoded)
        i = 0

        while i < length:
            try:
                if i + 2 < length:
                    # Decode three characters into two bytes
                    value = (
                        cls.ALPHABET.index(encoded[i])
                        + cls.ALPHABET.index(encoded[i + 1]) * cls.BASE
                        + cls.ALPHABET.index(encoded[i + 2]) * cls.BASE * cls.BASE
                    )
                    decoded_bytes.append(value >> 8)
                    decoded_bytes.append(value & 0xFF)
                    i += 3
                else:
                    # Decode the last two characters into one byte
                    value = (
                        cls.ALPHABET.index(encoded[i])
                        + cls.ALPHABET.index(encoded[i + 1]) * cls.BASE
                    )
                    decoded_bytes.append(value)
                    i += 2
            except ValueError:
                raise ValueError("Invalid character in Base45 string")

        return bytes(decoded_bytes)
