from struct import *

f = open("compressed.bin" ,"rb")
byte = f.read(2)
count = 1
while byte != "":
    offset_and_length = unpack(">H", byte)
    offset = offset_and_length[0] >> 6
    length = offset_and_length[0] - (offset << 6)
    print "Length "+str(length)
    print "Offset "+str(offset)
    char = f.read(1)
    print "Char "+str(char)
    byte = f.read(2)
    count += 1
