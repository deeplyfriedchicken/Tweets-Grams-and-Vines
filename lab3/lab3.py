# Kevin Cunanan
# username: kcunanan
# Lab1

import operator
import json
from heapq import merge
import math # log functions
import sys # necessary to call read file

def huff(lst, acc, code):
    if len(lst) == 1:
        code.append((lst, acc))
    else:
        left = huff(lst[0], acc + "0", code)
        right = huff(lst[1], acc + "1", code)

def main():
    dict1 = {}
    with open(str(sys.argv[1]), 'rb') as textFile:
        for line in textFile:
            chars = list(line)
            for val in chars:
                if val in dict1:
                    dict1[val] += 1
                else:
                    dict1[val] = 1
    for key, value in dict1.iteritems(): #iterate through items in dict1
        if len(key) == 1: # if not it's a non-printable we've gone thru
            if ord(key) < 32 or ord(key) >= 127:
                dict1[str(hex(ord(key)))] = dict1[key]
                del dict1[key]
    lst = dict1.items()
    lst = sorted(lst, key=lambda y:y[1])
    print lst
    while len(lst) > 1:
        z = lst[0]
        y = lst[1]
        v = z[1] + y[1]
        k = [z[0], y[0]]
        lst = list(merge(lst[2:], [(k,v)]))
    tree = lst[0][0]
    print tree
    code = []
    huff(tree, "", code)
    huffman = dict(code)
    for key, value in huffman.iteritems():
        if len(str(key)) == 1:
            huffman[ord(str(key))] = huffman[key]
            del huffman[key]
    print json.dumps(huffman, indent=4, separators=(',',': ')) # for pretty JSON output
main()
