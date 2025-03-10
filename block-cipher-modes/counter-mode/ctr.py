import argparse
from typing import Optional


class CTRMode:
    """
    A class to implement the Counter Mode (CTR) for block ciphers.
    """

    def __init__(self, key: int, block_size: int = 16):
        """
        Initialize the CTRMode class.

        Attributes:
            key (int): The encryption key.
            block_size (int): The size of the block in bytes (default is 16).
        """
        if not isinstance(key, int) or key <= 0:
            raise ValueError("Key must be a positive integer.")
        if not isinstance(block_size, int) or block_size <= 0:
            raise ValueError("Block size must be a positive integer.")

        self.key = key
        self.block_size = block_size

    def _encrypt_block(self, block: bytes, counter: int) -> bytes:
        """
        Encrypt a single block using a simple XOR operation with the key and counter.

        Args:
            block (bytes): The block to encrypt.
            counter (int): The counter value.

        Returns:
            bytes: The encrypted block.
        """
        if len(block) != self.block_size:
            raise ValueError(f"Block size must be {self.block_size} bytes.")

        # Simulate encryption by XORing the block with the key and counter
        encrypted_block = bytes([b ^ ((self.key + counter) % 256) for b in block])
        return encrypted_block

    def encrypt(self, plaintext: bytes, nonce: Optional[int] = None) -> bytes:
        """
        Encrypt the plaintext using Counter Mode (CTR).

        Args:
            plaintext (bytes): The plaintext to encrypt.
            nonce (Optional[int]): A unique value for the encryption. If None, a default is used.

        Returns:
            bytes: The ciphertext.
        """
        if not isinstance(plaintext, bytes):
            raise ValueError("Plaintext must be in bytes format.")

        if nonce is None:
            nonce = 0  # Default nonce value

        ciphertext = bytearray()
        counter = 0

        # Process the plaintext in blocks
        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i : i + self.block_size]
            if len(block) < self.block_size:
                # Pad the last block if necessary
                block += bytes([0] * (self.block_size - len(block)))

            # Encrypt the block
            encrypted_block = self._encrypt_block(block, nonce + counter)
            ciphertext.extend(encrypted_block)
            counter += 1

        return bytes(ciphertext)

    def decrypt(self, ciphertext: bytes, nonce: Optional[int] = None) -> bytes:
        """
        Decrypt the ciphertext using Counter Mode (CTR).

        Args:
            ciphertext (bytes): The ciphertext to decrypt.
            nonce (Optional[int]): The nonce used during encryption. If None, a default is used.

        Returns:
            bytes: The plaintext (bytes).
        """
        # CTR mode decryption is the same as encryption
        return self.encrypt(ciphertext, nonce)


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = argparse.ArgumentParser(
        description="Counter Mode (CTR) Encryption/Decryption"
    )
    parser.add_argument(
        "--key", type=int, required=True, help="Encryption key (integer)"
    )
    parser.add_argument(
        "--action",
        type=str,
        required=True,
        choices=["encrypt", "decrypt"],
        help="Action to perform: encrypt or decrypt",
    )
    parser.add_argument("--input", type=str, required=True, help="Input file path")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    parser.add_argument("--nonce", type=int, help="Nonce value (integer)")
    args = parser.parse_args()

    try:
        # Read the input file
        with open(args.input, "rb") as f:
            data = f.read()

        # Initialize CTRMode
        ctr = CTRMode(key=args.key)

        # Perform the action
        if args.action == "encrypt":
            result = ctr.encrypt(data, args.nonce)
        else:
            result = ctr.decrypt(data, args.nonce)

        # Write the result to the output file
        with open(args.output, "wb") as f:
            f.write(result)

        print(
            f"{args.action.capitalize()}ion completed successfully. Output saved to {args.output}"
        )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
