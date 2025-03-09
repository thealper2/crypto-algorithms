class ReverseCipher:
    """
    A class to implement the Reverse Cipher.
    """

    def __init__(self):
        """
        Initialize the ReverseCipher object with the input text.
        """
        pass

    def _reverse_text(self, text: str) -> str:
        """
        Reverse the input text.

        Args:
            text (str): The text to be reversed.

        Returns:
            str: The reversed text.
        """
        reversed_text = ""
        for i in range(len(text) - 1, -1, -1):  # Iterate from the end to the start
            reversed_text += text[i]

        return reversed_text

    def encrypt(self, text: str) -> str:
        """
        Encrypt the text by reversing it.

        Args:
            text (str): The text to be reversed.

        Returns:
            str: The reversed (encrypted) text.
        """
        return self._reverse_text(text)

    def decrypt(self, text: str) -> str:
        """
        Decrypt the text by reversing it back to the original.

        Args:
            text (str): The text to be reversed.

        Returns:
            str: The original text.
        """
        return self._reverse_text(text)
