class Fletcher:
    """
    A class to compute the Fletcher checksum for a given input string.
    """

    def __init__(self, data: str):
        """
        Initialize the Fletcher class with the input data.

        Attributes:
            data (str): The input string for which the checksum will be computed.
        """
        self.data = data

    def compute_checksum(self) -> int:
        """
        Compute the Fletcher checksum for the input data.

        Returns:
            int: The computed checksum as an integer.

        Raises:
            ValueError: If the input data is empty.
        """
        if not self.data:
            raise ValueError("Input data cannot be empty.")

        sum1 = 0
        sum2 = 0

        for char in self.data:
            # Convert the character to its ASCII value
            ascii_value = ord(char)
            sum1 = (sum1 + ascii_value) % 255
            sum2 = (sum2 + sum1) % 255

        # The Fletcher checksum is a combination of sum1 and sum2
        checksum = (sum2 << 8) | sum1
        return checksum

    @staticmethod
    def validate_checksum(data: str, checksum: int) -> bool:
        """
        Validate the Fletcher checksum for the given data.

        Args:
            data (str): The input string to validate.
            checksum (int): The checksum to validate against.

        Returns:
            bool: True if the checksum is valid, False otherwise.
        """
        fletcher = Fletcher(data)
        computed_checksum = fletcher.compute_checksum()
        return computed_checksum == checksum
