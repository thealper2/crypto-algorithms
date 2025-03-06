import numpy as np

from hill_cipher import HillCipher
from utils import setup_argparser


def main():
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        key_list = list(map(int, args.key.split(",")))
        key_matrix = np.array(key_list).reshape(int(len(key_list) ** 0.5), -1)
        hill_cipher = HillCipher(key_matrix)

        if args.mode == "encrypt":
            result = hill_cipher.encrypt(args.text)
            print(f"Encrypted: {result}")
        elif args.mode == "decrypt":
            result = hill_cipher.decrypt(args.text)
            print(f"Decrypted: {result}")
        else:
            print("Please specify encrypt or decrypt.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
