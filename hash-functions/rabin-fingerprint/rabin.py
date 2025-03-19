from typing import Optional


class RabinFingerprint:
    """
    A class to compute the Rabin Fingerprint of a given input string or byte sequence.

    Attributes:
        base (int): The base value for the polynomial rolling hash.
        modulus (int): The modulus value to keep the hash within a fixed range.
    """

    def __init__(self, base: int = 256, modulus: int = 101):
        """
        Initialize the RabinFingerprint class with a base and modulus.

        Args:
            base (int): The base value for the polynomial rolling hash. Default is 256.
            modulus (int): The modulus value to keep the hash within a fixed range. Default is 101.
        """
        self.base = base
        self.modulus = modulus

    def compute(self, data: str) -> Optional[int]:
        """
        Compute the Rabin Fingerprint for the given input data.

        Args:
            data (str): The input string or byte sequence to compute the fingerprint for.

        Returns:
            Optional[int]: The computed fingerprint as an integer, or None if the input is empty.
        """
        if not data:
            return None

        fingerprint = 0
        try:
            for char in data:
                # Update the fingerprint using the polynomial rolling hash formula.
                fingerprint = (fingerprint * self.base + ord(char)) % self.modulus
        except Exception as e:
            print(f"An error occurred while computing the fingerprint: {e}")
            return None

        return fingerprint

    def rolling_hash(
        self, old_char: str, new_char: str, prev_hash: int
    ) -> Optional[int]:
        """
        Compute the rolling hash for a new character given the previous hash and the old character.

        Args:
            old_char (str): The character being removed from the window.
            new_char (str): The character being added to the window.
            prev_hash (int): The previous hash value.

        Returns:
            Optional[int]: The updated rolling hash, or None if an error occurs.
        """
        if not old_char or not new_char:
            return None

        try:
            # Remove the contribution of the old character and add the new character
            new_hash = (
                prev_hash - ord(old_char) * (self.base ** (len(old_char) - 1))
            ) % self.modulus
            new_hash = (new_hash * self.base + ord(new_char)) % self.modulus
        except Exception as e:
            print(f"An error occurred while computing the rolling hash: {e}")
            return None

        return new_hash
