import sys
import argparse


class ECBMode:
    """
    A simple implementation of Electronic Codebook (ECB) mode for block ciphers.
    """

    BLOCK_SIZE = 16  # 128-bit block size

    def __init__(self, key: bytes):
        """
        Initialize ECB mode with a given key.

        Attributes:
            key (bytes): The encryption key (must be 16 bytes long).
        """
        if len(key) != self.BLOCK_SIZE:
            raise ValueError("Key must be exactly 16 bytes long.")
        self.key = key

    def _pad(self, data: bytes) -> bytes:
        """
        Pad the data using PKCS#7 padding.


        Args:
            data (bytes): The data to be padded.

        Returns:
            bytes: Padded data.
        """
        pad_length = self.BLOCK_SIZE - (len(data) % self.BLOCK_SIZE)
        return data + bytes([pad_length] * pad_length)

    def _unpad(self, data: bytes) -> bytes:
        """
        Remove PKCS#7 padding from data.

        Args:
            data (bytes): The padded data.

        Returns:
            bytes: Unpadded data.
        """
        pad_length = data[-1]
        if pad_length < 1 or pad_length > self.BLOCK_SIZE:
            raise ValueError("Invalid padding detected.")
        return data[:-pad_length]

    def _xor(self, block: bytes, key: bytes) -> bytes:
        """
        XOR operation to simulate a simple block cipher encryption.

        Args:
            block (bytes): The input block (16 bytes).
            key (bytes): The encryption key (16 bytes).

        Returns:
            bytes: XORed result.
        """
        return bytes(b ^ k for b, k in zip(block, key))

    def encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt the plaintext using ECB mode.

        Args:
            plaintext (bytes): The plaintext data to encrypt.

        Returns:
            bytes: Encrypted ciphertext.
        """
        padded_text = self._pad(plaintext)
        ciphertext = b""

        for i in range(0, len(padded_text), self.BLOCK_SIZE):
            block = padded_text[i : i + self.BLOCK_SIZE]
            encrypted_block = self._xor(block, self.key)
            ciphertext += encrypted_block

        return ciphertext

    def decrypt(self, ciphertext: bytes) -> bytes:
        """
        Decrypt the ciphertext using ECB mode.

        Args:
            ciphertext (bytes): The encrypted data.

        Returns:
            bytes: Decrypted plaintext.
        """
        if len(ciphertext) % self.BLOCK_SIZE != 0:
            raise ValueError("Ciphertext length is not a multiple of block size.")

        plaintext = b""

        for i in range(0, len(ciphertext), self.BLOCK_SIZE):
            block = ciphertext[i : i + self.BLOCK_SIZE]
            decrypted_block = self._xor(block, self.key)
            plaintext += decrypted_block

        return self._unpad(plaintext)


def main():
    parser = argparse.ArgumentParser(description="ECB Mode Encryption/Decryption")
    parser.add_argument(
        "mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt"
    )
    parser.add_argument(
        "input",
        type=str,
        help="Input text (for encryption: plaintext, for decryption: hex ciphertext)",
    )
    parser.add_argument("--key", type=str, help="16-byte key for encryption/decryption")

    args = parser.parse_args()

    # Convert key to bytes
    key = args.key.encode()
    if len(key) != ECBMode.BLOCK_SIZE:
        print("Error: Key must be exactly 16 bytes long.")
        sys.exit(1)

    ecb = ECBMode(key)

    if args.mode == "encrypt":
        plaintext = args.input.encode()
        ciphertext = ecb.encrypt(plaintext)
        print("Encrypted (Hex):", ciphertext.hex())

    elif args.mode == "decrypt":
        try:
            ciphertext = bytes.fromhex(args.input)
            plaintext = ecb.decrypt(ciphertext)
            print("Decrypted:", plaintext.decode())
        except ValueError as e:
            print(f"Decryption error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
