#!/usr/bin/env python3
import time
import sys

def get_parameters():
    if len(sys.argv) != 2:
        print("usage: ./attack_server <Attacker port>")
        exit(-1)

    return sys.argv[1]


def main():
    attacker_port = get_parameters()


if __name__ == '__main__':
    main()