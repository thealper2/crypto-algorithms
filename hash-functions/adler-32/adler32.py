from typing import Union


class Adler32:
    """
    A class to compute the Adler-32 checksum of a given input data.
    """

    MOD_ADLER = 65521  # Largest prime number smaller than 2^16

    def __init__(self):
        """
        Initialize the Adler32 class.
        """
        self._a = 1
        self._b = 0

    def update(self, data: Union[bytes, bytearray]) -> None:
        """
        Update the Adler-32 checksum with new data.

        Args:
            data (Union[bytes, bytearray]): The input data to compute the checksum for.

        Raises:
            TypeError: If the input data is not of the type bytes or bytearray.
        """
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("Input data must be of type bytes or bytearray.")

        for byte in data:
            self._a = (self._a + byte) % self.MOD_ADLER
            self._b = (self._b + self._a) % self.MOD_ADLER

    def digest(self) -> int:
        """
        Return the computed Adler-32 checksum as an integer.

        Returns:
            int: The computed Adler-32 checksum.
        """
        return (self._b << 16) | self._a

    def hexdigest(self) -> str:
        """
        Return the computed Adler-32 checksum as a hexadecimal string.

        Returns:
            str: The computed Adler-32 checksum in hexadecimal format.
        """
        return f"{self.digest():08x}".upper()

    def reset(self) -> None:
        """
        Reset the Adler-32 checksum to its initial state.
        """
        self._a = 1
        self._b = 0
