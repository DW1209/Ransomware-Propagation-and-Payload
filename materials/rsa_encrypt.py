import sys
import pickle


def get_parameters():
    if len(sys.argv) != 4:
        print(f'python3 {__file__} <n> <e> <file>')
        exit(-1)
    return int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]


def main():
    n, e, filename = get_parameters()

    plain_bytes = b''
    with open(filename, 'rb') as f:
        plain_bytes = f.read()

    cipher_int = [pow(i, e, n) for i in plain_bytes]
    with open(filename, 'wb') as f:
        pickle.dump(cipher_int, f)


if __name__ == '__main__':
    main()