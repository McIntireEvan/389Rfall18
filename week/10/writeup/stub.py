#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct

# TODO: Potential improvements
# - Prompt user for message/malicious
# - Improved parsing now that we know the format
# - Break on correct answer

#####################################
### STEP 1: Calculate forged hash ###
#####################################

# Connect
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('142.93.118.186', 1234))

# Get prompt
res = sock.recv(1024)

# Go to signing prompt
sock.send('1\n')
res = sock.recv(1024)

# Sign the message
message = 'Hello!'
sock.send(message + '\n')

# Get our response
res = sock.recv(1024)

# From the response, grab our hash
legit = res.split(' ')[-1]
print 'Actual hash:'
print legit

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.strip().decode('hex'))

malicious = 'Hack the planet'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print 'Fake hash:'
print(fake_hash)

#############################
### STEP 2: Craft payload ###
#############################

# consume the menu
res = sock.recv(1024)
print '=========================='
for i in range(6, 16):
    print 'Attempting with i = ' + str(i)
    # First, compute stuff

    # Padding
    # Overall, we should have 64 bytes
    # 8 go to the length (l1), 64 - 8 = 56
    # Then, in the padding itself, 1 byte goes to 1 (\x80), so we're down to at most 55 \x00's
    # For those, we know the secret is somewhere between 6 and 16 bytes, and we know the length of our message
    # We can multiply a string by a number to repeat it! Who knew?
    padding = '\x80' + ('\x00' * (55 - len(message) - i))

    # Need to put the len(secret + message) in little endian
    # see https://stackoverflow.com/questions/13141787/convert-decimal-int-to-little-endian-string-x-x
    length = struct.pack('<Q', (i + len(message)) * 8)

    # Construct payload
    payload = message + padding + length + malicious

    # Go to the hash checker
    sock.send('2\n')
    res = sock.recv(1024)

    # Send the constructed hash
    sock.send(fake_hash + '\n')
    res = sock.recv(1024)

    # Send the payload
    sock.send(payload + '\n')
    res = sock.recv(1024)

    # Parse the response, check for failure, print results otherwide
    res = sock.recv(1024)
    if 'Hmm...' in res:
        print 'Failed'
    else:
        print res
    print '=========================='
