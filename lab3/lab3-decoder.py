import operator
import json
import struct
from heapq import merge
import math # log functions
import sys # necessary to call read file
import md5
import os

f = open('huffpressed.txt' ,"rb")
head1 = json.loads(f.readline())
print head1['hash']
print head1['size']

huffman_old = json.loads(f.readline())

huffman = {}
for key, value in huffman_old.iteritems():
    huffman[value] = key
print huffman

binary = ""
byte = f.read(1)
while byte != "":
    format(byte, '08b')
    byte = f.read(1)
print binary
