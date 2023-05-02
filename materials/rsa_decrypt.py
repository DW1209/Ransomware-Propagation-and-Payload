import sys
import pickle


def get_parameters():
    if len(sys.argv) != 4:
        print(f'python3 {__file__} <n> <d> <file>')
        exit(-1)
    return int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]


def main():
    n, d, filename = get_parameters()

    with open(filename, 'rb') as f:
        cipher_int = pickle.load(f)
        decrypted_int = [pow(i, d, n) for i in cipher_int]
        decrypted_bytes = bytes(decrypted_int)
        
    with open(filename, 'wb') as f:
        f.write(decrypted_bytes)


if __name__ == '__main__':
    main()