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
    if length == 0:
        buf.append(char)
    else:
        for i in range (0, length+1):
            buf.append(buf[i+offset])
    byte = f.read(2)
print buf
for i in range (0,len(buf)):
    w.write(buf[i])
