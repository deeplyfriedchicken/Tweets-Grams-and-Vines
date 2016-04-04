# Kevin Cunanan
# username: kcunanan
# Lab3

import operator
import json
import struct
from heapq import merge
import sys # necessary to call read file
import md5
import os

#1.3
def huff(lst, acc, code): # uses a binary tree to assign codes to keys
    if len(lst) == 1:
        code.append((lst, acc))
    else:
        left = huff(lst[0], acc + "0", code)
        right = huff(lst[1], acc + "1", code)

def main():
    #1.2
    dict1 = {}
    input_file = sys.argv[1]
    idx = input_file.find(".")
    huff_input = input_file[0:idx]
    file_type = input_file[idx:]

    with open(input_file, 'rb') as textFile:
        for line in textFile:
            chars = list(line)
            for val in chars:
                if val in dict1:
                    dict1[val] += 1
                else:
                    dict1[val] = 1
    lst = dict1.items()
    lst = sorted(lst, key=lambda y:y[1])
    while len(lst) > 1:
        z = lst[0]
        y = lst[1]
        v = z[1] + y[1]
        k = [z[0], y[0]]
        lst.append([k,v])
        lst = sorted(lst[2:], key=lambda y:y[1]) # sorts a balanced tree
    tree = lst[0][0]
    code = []
    huff(tree, "", code)
    huffman = dict(code)
    for key, value in huffman.iteritems():
        if len(str(key)) == 1:
            huffman[ord(str(key))] = huffman[key]
            del huffman[key]
    # 2.1
    f = open(input_file ,"rb")
    butts = "" # string to hold binary data
    cats = f.read(1) # reads a character in input file
    while cats != "":
        if ord(str(cats)) < 32:
            cats = ord(str(cats))
            butts += huffman[cats]
        else:
            butts += huffman[ord(str(cats))]
        cats = f.read(1)
    if len(butts) % 8 != 0:
        remainder = len(butts) % 8
        for i in range(0, 8-remainder):
            butts = butts + "0"
    if len(butts) % 8 == 0:
        print "Binary String OK"
    else:
        raise ValueError("Binary String is not a multiple of 8")
    # 2.2
    deets = {}
    deets['size'] = os.path.getsize(input_file)
    g = open(input_file ,"rb")
    feed = g.read(4096)
    m = md5.new()
    while feed != "":
        m.update(feed)
        feed = g.read(4096)
    deets['hash'] = m.hexdigest()
    deets['type'] = file_type
    deets['name'] = huff_input
    # print deets['hash']
    w = open(huff_input + '.huf', "wb")
    w.write(json.dumps(deets))
    w.write("\n")
    w.write(json.dumps(huffman))
    w.write("\n")
    loops = list(butts)
    tot = float(len(butts))
    integer = str(''.join(loops[0:8]))
    print "Compressing..."
    while integer != "":
        progress = round(100 - 100*(float(len(loops))/tot), 2) # Progress bar
        sys.stdout.write("\r"+ str(progress) + "% completed" )
        sys.stdout.flush()
        new = int(integer,2)
        w.write(struct.pack("B",new))
        loops = loops[8:]
        integer = str(''.join(loops[0:8]))
    print ""
    print input_file + " compression complete."
    size = float(os.path.getsize(huff_input + '.huf'))
    ratio = float(deets['size'])/size
    print "Compression Ratio: " + str(ratio)
main()
