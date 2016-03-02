# Kevin Cunanan
# decompress
from struct import *
import sys

f = open(str(sys.argv[1]) ,"rb")
w = open(str('uncompressed.bin'), "wb")
byte = f.read(2)
char = f.read(1)
buf = []
while byte != "":
    offset_and_length = unpack(">H", byte)
    offset = offset_and_length[0] >> 6
    length = offset_and_length[0] - (offset << 6)
    print "Length "+str(length)
    print "Offset "+str(offset)
    if length == 0:
        buf.append(char)
    else:
        copy_idx = offset
        for i in range (0, length):
            buf.append(buf[copy_idx + i])
        buf.append(char)
    byte = f.read(2)
    char = f.read(1)
print buf
w.write(''.join(buf))
