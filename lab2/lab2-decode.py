# Kevin Cunanan
# decoder
from struct import *
import sys

f = open(str(sys.argv[1]) ,"rb")
w = open(str('uncompressed.bin'), "wb")
both = unpack(">H", f.read(2))
shift = both[0]
both = unpack(">H", f.read(2))
N = both[0]
print N
byte = f.read(2)
char = f.read(1)

buf = []
copy_idx = 0
while byte != "":
    if len(buf) > N:
        copy_idx = len(buf) - N
    offset_and_length = unpack(">H", byte)
    offset = offset_and_length[0] >> shift
    length = offset_and_length[0] - (offset << shift)
    if length == 0:
        buf.append(char)
    else:
        for i in range (0, length):
            buf.append(buf[copy_idx + offset + i])
        buf.append(char)
    byte = f.read(2)
    char = f.read(1)
w.write(''.join(buf))
