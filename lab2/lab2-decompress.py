# Kevin Cunanan
# decompress
from struct import *
import sys

f = open(str(sys.argv[1]) ,"rb")
w = open(str('uncompressed.bin'), "wb")
byte = f.read(2)
count = 1
buf = []
while byte != "":
    offset_and_length = unpack(">H", byte)
    offset = offset_and_length[0] >> 6
    length = offset_and_length[0] - (offset << 6)
    char = f.read(1)
    print "Length "+str(length)
    print "Offset "+str(offset)
    count = 0
    while length >= 0:
        if length == 0:
            buf.append(char)
            w.write(char)
        else:
            buf.append(buf[offset + count])
            w.write(char)
        count += 1
        length = length - 1
    byte = f.read(2)
    count += 1
print buf
