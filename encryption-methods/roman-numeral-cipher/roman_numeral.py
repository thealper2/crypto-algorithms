class RomanNumeralCipher:
    """
    A class to encode and decode text using the Roman Numeral cipher.
    """

    # Mapping of letters to Roman numerals
    LETTER_TO_ROMAN = {
        "A": "I",
        "B": "II",
        "C": "III",
        "D": "IV",
        "E": "V",
        "F": "VI",
        "G": "VII",
        "H": "VIII",
        "I": "IX",
        "J": "X",
        "K": "XI",
        "L": "XII",
        "M": "XIII",
        "N": "XIV",
        "O": "XV",
        "P": "XVI",
        "Q": "XVII",
        "R": "XVIII",
        "S": "XIX",
        "T": "XX",
        "U": "XXI",
        "V": "XXII",
        "W": "XXIII",
        "X": "XXIV",
        "Y": "XXV",
        "Z": "XXVI",
    }

    # Reverse mapping of Roman numerals to letters
    ROMAN_TO_LETTER = {v: k for k, v in LETTER_TO_ROMAN.items()}

    def __init__(self):
        """
        Initialize the RomanNumeralCipher class.
        """
        pass

    def encode(self, text: str) -> str:
        """
        Encode the input text into Roman numerals.

        Args:
            text (str): The text to encode.

        Returns:
            str: The encoded Roman numeral string.

        Raises:
            ValueError: If the input text contains non-alphabetic characters.
        """
        if not text.isalpha():
            raise ValueError("Input text must contain only alphabetic characters.")

        text = text.upper()  # Convert to uppercase for consistency
        encoded_text = []

        for char in text:
            if char in self.LETTER_TO_ROMAN:
                encoded_text.append(self.LETTER_TO_ROMAN[char])
            else:
                encoded_text.append("")  # Handle spaces or unsupported characters

        return " ".join(encoded_text)

    def decode(self, encoded_text: str) -> str:
        """
        Decode the Roman numeral string back into text.

        Args:
            encoded_text (str): The Roman numeral string to decode.

        Returns:
            str: The decoded text.

        Raises:
            ValueError: If the input contains invalid Roman numerals.
        """
        roman_numerals = encoded_text.split()
        decoded_text = []

        for numeral in roman_numerals:
            if numeral in self.ROMAN_TO_LETTER:
                decoded_text.append(self.ROMAN_TO_LETTER[numeral])
            else:
                raise ValueError(f"Invalid Roman numeral: {numeral}")

        return "".join(decoded_text)
