#!/usr/bin/env python2

import sys
import struct

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

file_index = 0

def write_png(data):
    global file_index
    png = open(str(file_index) + '.png', "wb+")
    png.write(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
    png.write(data)

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestamp = struct.unpack("<L", data[8:12])[0]
try:
    timestamp = int(timestamp)
except ValueError:
    bork("Timestamp is not valid")

author = struct.unpack("<8s", data[12:20])

section_count = struct.unpack("<L", data[20:24])[0]

if(int(section_count) < 0):
    bork("Cannot have negative sections")

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % timestamp)
print("AUTHOR: %s" % author)
print("SECTION COUNT: %s" % section_count)

index = 24

print("-------  BODY  -------")

j = 1
while index + 8 < len(data):
    print("Section " + str(j))
    print("------")
    j += 1
    stype, slen = struct.unpack("<LL", data[index:index + 8])
    index += 8

    if stype == 0x1:
        print('Type: PNG')
        write_png(data[index:index+slen])
        print('Wrote png to ' + str(j) + '.pg')
    elif stype == 0x2:
        print('Type: DWORDS')
    elif stype == 0x3:
        print('Type: UTF-8')
        text = struct.unpack("<"+str(slen)+"s", dataprint()[index:index+slen])[0]
        print("Contents: " + text.decode("utf-8"))
    elif stype == 0x4:
        print('Type: DOUBLES')
    elif stype == 0x5:
        print('Type: WORDS')
    elif stype == 0x6:
        print('Type: COORD')
    elif stype == 0x7:
        print('Type: REFERENCE')
        if(slen != 4):
            bork("Invalid length")
        ref = struct.unpack("<L", data[index:index+slen])[0]
        if(ref < 0 or ref > section_count):
            bork("Invalid section reference")

        print("Points to section: " + str(ref))
    elif stype == 0x9:
        print('Type: ASCII')
        text = struct.unpack("<"+str(slen)+"s", data[index:index+slen])[0]
        print("Contents: " + text.decode())
    else:
        bork("Invalid section type")


    index += (slen)