class Base62Cipher:
    """
    A class to encode and decode integers to/from Base62 format.
    """

    # Define the Base62 character set
    BASE62_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    BASE = len(BASE62_CHARS)

    def __init__(self):
        """Initialize the Base62Cipher class."""
        self.char_to_value = {char: idx for idx, char in enumerate(self.BASE62_CHARS)}
        self.value_to_char = {idx: char for idx, char in enumerate(self.BASE62_CHARS)}

    def encode(self, number: int) -> str:
        """
        Encode a positive integer into a Base62 string.

        Args:
            number (int): The positive integer to encode.

        Returns:
            str: The Base62 encoded string.

        Raises:
            ValueError: If the input number is not a positive integer.
        """
        if not isinstance(number, int) or number < 0:
            raise ValueError("Input must be a non-negative integer.")

        if number == 0:
            return self.BASE62_CHARS[0]

        encoded = []
        while number > 0:
            remainder = number % self.BASE
            encoded.append(self.value_to_char[remainder])
            number = number // self.BASE

        return "".join(reversed(encoded))

    def decode(self, encoded_str: str) -> int:
        """
        Decode a Base62 string into a positive integer.

        Args:
            encoded_str (str): The Base62 encoded string.

        Returns:
            int: The decoded positive integer.

        Raises:
            ValueError: If the input string contains invalid Base62 characters.
        """
        if not isinstance(encoded_str, str) or not encoded_str:
            raise ValueError("Input must be a non-empty string.")

        decoded = 0
        for char in encoded_str:
            if char not in self.char_to_value:
                raise ValueError(f"Invalid character '{char}' in Base62 string.")
            decoded = decoded * self.BASE + self.char_to_value[char]

        return decoded
