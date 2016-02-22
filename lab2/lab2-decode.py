from struct import *

f = open("compressed.bin" ,"rb")
byte = f.read(2)
count = 1
while byte != "":
    offset_and_length = unpack(">H", byte)
    print offset_and_length
    char = f.read(1)
    print char
    byte = f.read(2)
    count += 1
