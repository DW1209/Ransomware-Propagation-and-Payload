#!/usr/bin/env python3

import sys
import time


def get_parameters():
    if len(sys.argv) != 2:
        print(f"usage: {__file__} <Attacker port>")
        exit(-1)
    return sys.argv[1]


def main():
    attacker_port = get_parameters()
    print(f'Server listening on port {attacker_port} ...')
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('\nDetected CTRL + C pressed and exiting ...')
            return


if __name__ == '__main__':
    main()
