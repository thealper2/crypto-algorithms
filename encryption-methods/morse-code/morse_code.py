from typing import Dict, Optional


class MorseCodeCipher:
    """
    A class to handle Morse code encoding and decoding operations.
    """

    # Morse code dictionary
    MORSE_CODE_DICT: Dict[str, str] = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        " ": "/",
    }

    # Reverse Morse code dictionary for decoding
    REVERSE_MORSE_CODE_DICT: Dict[str, str] = {
        value: key for key, value in MORSE_CODE_DICT.items()
    }

    def __init__(self):
        """
        Initializes the MorseCodeCipher class.
        """
        pass

    def encode(self, text: str) -> Optional[str]:
        """
        Encodes the given text into Morse code

        Args:
            text (str): The text to be encoded.

        Returns:
            Optional[str]: The encoded Morse code string or None if an error occurs.
        """
        try:
            return " ".join(self.MORSE_CODE_DICT[char.upper()] for char in text)
        except KeyError as e:
            print(f"Error: Character '{e.args[0]}' cannot be encoded in Morse code.")
            return None

    def decode(self, morse_code: str) -> Optional[str]:
        """
        Decodes the given Morse code into text.

        Args:
            morse_code (str): The Morse code to be decoded.

        Returns:
            Optional[str]: The decoded text or None if an error occurs.
        """
        try:
            return "".join(
                self.REVERSE_MORSE_CODE_DICT[code] for code in morse_code.split(" ")
            )
        except KeyError as e:
            print(f"Error: Morse Code '{e.args[0]}' cannot be decoded.")
            return None
