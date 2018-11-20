#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re
import time

def do_hash(alg, data):
    ha = hashlib.new(str(alg))
    ha.update(match.group(2).encode('utf-8'))
    return ha.hexdigest()


host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    # Recieve and decode
    data = s.recv(1024)
    recv = data.decode().split('\n')

    # Pretty print
    for st in recv:
        print(st)

    # Exit on winning
    if "You win!" in data.decode():
        break

    # Find hash and algorithm to use
    match = re.search('Find me the (.+) hash of (.+)', data.decode())
    sol = str(do_hash(match.group(1), match.group(2)) + '\n').encode()

    # Print and send res
    print(sol)
    s.send(sol)

print("Exiting")
s.close()
