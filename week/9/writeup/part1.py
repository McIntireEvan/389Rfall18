#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashfile = open("../hashes", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

words = []
for word in wordlist:
    words.append(word.rstrip())

hashes = []
for h in hashfile:
    hashes.append(h.rstrip())

for salt in salts:
    for word in words:
        salted = str(salt + word).encode('utf-8')
        computed_hash = hashlib.sha512(salted).hexdigest()
        for h in hashes:
            if h == computed_hash:
                print("---------------------------")
                print("Match found!")
                print("Hash: " + h)
                print("Salt: " + salt)
                print("Password: " + word)
                print("---------------------------")
