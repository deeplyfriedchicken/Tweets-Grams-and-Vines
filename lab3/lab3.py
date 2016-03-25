# Kevin Cunanan
# username: kcunanan
# Lab3

import operator
import json
import struct
from heapq import merge
import math # log functions
import sys # necessary to call read file
import md5
import os

def huff(lst, acc, code):
    if len(lst) == 1:
        code.append((lst, acc))
    else:
        left = huff(lst[0], acc + "0", code)
        right = huff(lst[1], acc + "1", code)

def main():
    dict1 = {}
    input_file = sys.argv[1]
    with open(input_file, 'rb') as textFile:
        for line in textFile:
            chars = list(line)
            for val in chars:
                if val in dict1:
                    dict1[val] += 1
                else:
                    dict1[val] = 1
    # for key, value in dict1.iteritems(): #iterate through items in dict1
    #     if len(key) == 1: # if not it's a non-printable we've gone thru
    #         if ord(key) < 32 or ord(key) >= 127:
    #             dict1[str(hex(ord(key)))] = dict1[key]
    #             del dict1[key]
    lst = dict1.items()
    lst = sorted(lst, key=lambda y:y[1])
    while len(lst) > 1:
        z = lst[0]
        y = lst[1]
        v = z[1] + y[1]
        k = [z[0], y[0]]
        lst.append([k,v])
        lst = sorted(lst[2:], key=lambda y:y[1])
    tree = lst[0][0]
    code = []
    huff(tree, "", code)
    huffman = dict(code)
    for key, value in huffman.iteritems():
        if len(str(key)) == 1:
            huffman[ord(str(key))] = huffman[key]
            del huffman[key]
    # 2,1
    f = open(input_file ,"rb")
    butts = ""
    cats = f.read(1)
    print json.dumps(huffman, indent=4, separators=(',',': ')) # for pretty JSON output
    print cats
    while cats != "":
        print cats
        if ord(str(cats)) < 32:
            cats = ord(str(cats))
            butts += huffman[cats]
        else:
            butts += huffman[ord(str(cats))]
        cats = f.read(1)
    if len(butts)%8 != 0:
        remainder = len(butts) % 8
        for i in range(0, remainder):
            butts += "0"
    print butts
    print len(butts)%8
    # 2.3
    deets = {}
    deets['size'] = os.path.getsize(input_file)
    g = open(input_file ,"rb")
    feed = g.read(4096)
    m = md5.new()
    while feed != "":
        m.update(feed)
        feed = g.read(4096)
    deets['hash'] = m.hexdigest()
    print deets['hash']
    w = open('huffpressed.txt', "wb")
    w.write(json.dumps(deets))
    w.write("\n")
    w.write(json.dumps(huffman))
    w.write("\n")
    loops = list(butts)
    count = 0
    integer = str(''.join(loops[count:count+8]))
    while integer != "":
        print integer
        print count
        new = int(integer,2)
        w.write(str(new))
        w.write("\n")
        print new
        count += 8
        loops = loops[count:]
        integer = str(''.join(loops[count:count+8]))
main()
