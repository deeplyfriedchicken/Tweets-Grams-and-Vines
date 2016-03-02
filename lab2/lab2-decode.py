# Kevin Cunanan
# decompress
from struct import *
import sys

f = open(str(sys.argv[1]) ,"rb")
w = open(str('uncompressed.bin'), "wb")
byte = f.read(2)
char = f.read(1)
buf = []
copy_idx = 0
while byte != "":
    if len(buf) > 1024:
        copy_idx = len(buf) - 1024
    offset_and_length = unpack(">H", byte)
    offset = offset_and_length[0] >> 6
    length = offset_and_length[0] - (offset << 6)
    print "Length " + str(length)
    print "Offset " + str(offset)
    if length == 0:
        buf.append(char)
    else:
        for i in range (0, length):
            buf.append(buf[copy_idx + offset + i])
        buf.append(char)
    byte = f.read(2)
    char = f.read(1)
print buf
w.write(''.join(buf))
