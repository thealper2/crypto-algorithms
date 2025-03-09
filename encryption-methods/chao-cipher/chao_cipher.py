class ChaoCipher:
    """
    A class to implement the Chaocipher encryption and decryption algorithm.

    Attributes:
        left_alphabet (str): The left disk alphabet.
        right_alphabet (str): The right disk alphabet.
    """

    def __init__(self, left_alphabet: str, right_alphabet: str) -> None:
        """
        Initialize the ChaoCipher with the left and right alphabets.

        Args:
            left_alphabet (str): The alphabet for the left disk.
            right_alphabet (str): The alphabet for the right disk.

        Raises:
            ValueError: If the alphabets are not of the same length or contain duplicates.
        """
        if len(left_alphabet) != len(right_alphabet):
            raise ValueError("Alphabets must be of the same length.")
        if len(set(left_alphabet)) != len(left_alphabet) or len(
            set(right_alphabet)
        ) != len(right_alphabet):
            raise ValueError("Alphabets must not contain duplicate characters.")

        self.left_alphabet = left_alphabet
        self.right_alphabet = right_alphabet

    def _permute_alphabet(self, alphabet: str, index: int) -> str:
        """
        Permute the alphabet based on the Chaocipher rules.

        Args:
            alphabet (str): The alphabet to permute.
            index (int): The index to use for permutation.

        Returns:
            str: The permuted alphabet.
        """
        # Split the alphabet into two parts and rearrange
        return alphabet[index:] + alphabet[:index]

    def _shift_alphabet(self, alphabet: str) -> str:
        """
        Shift the alphabet by moving the second character to the end.

        Args:
            alphabet (str): The alphabet to shift.

        Returns:
            str: The shifted alphabet.
        """
        return alphabet[0] + alphabet[2:] + alphabet[1]

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the given plaintext using the Chaocipher algorithm.

        Args:
            plaintext (str): The text to encrypt.

        Returns:
            str: The encrypted ciphertext.
        """
        ciphertext = []
        for char in plaintext:
            if char not in self.right_alphabet:
                raise ValueError(f"Character '{char}' not found in the right alphabet.")

            # Find the index of the character in the right alphabet
            index = self.right_alphabet.index(char)
            # Append the corresponding character from the left alphabet
            ciphertext.append(self.left_alphabet[index])

            # Permute the alphabets
            self.left_alphabet = self._permute_alphabet(self.left_alphabet, index)
            self.right_alphabet = self._permute_alphabet(self.right_alphabet, index)

            # Shift the alphabets
            self.left_alphabet = self._shift_alphabet(self.left_alphabet)
            self.right_alphabet = self._shift_alphabet(self.right_alphabet)

        return "".join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the given ciphertext using the Chaocipher algorithm.

        Args:
            ciphertext (str): The text to decrypt.

        Returns:
            str: The decrypted plaintext.
        """
        plaintext = []
        for char in ciphertext:
            if char not in self.left_alphabet:
                raise ValueError(f"Character '{char}' not found in the left alphabet.")

            # Find the index of the character in the left alphabet
            index = self.left_alphabet.index(char)
            # Append the corresponding character from the right alphabet
            plaintext.append(self.right_alphabet[index])

            # Permute the alphabets
            self.left_alphabet = self._permute_alphabet(self.left_alphabet, index)
            self.right_alphabet = self._permute_alphabet(self.right_alphabet, index)

            # Shift the alphabets
            self.left_alphabet = self._shift_alphabet(self.left_alphabet)
            self.right_alphabet = self._shift_alphabet(self.right_alphabet)

        return "".join(plaintext)
