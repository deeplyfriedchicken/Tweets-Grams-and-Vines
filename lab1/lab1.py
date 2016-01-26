# Kevin Cunanan
# username: kcunanan
# Lab1

import json # json help
import math # log functions
import sys # necessary to call read file

dict1 = {}
with open(str(sys.argv[1]), 'rb') as textFile:
    for line in textFile:
        chars = list(unicode(line, errors='ignore')) # eliminates weird beginning characters that break the ASCII conversion
        for val in chars:
            if val in dict1:
                dict1[val] += 1
            else:
                dict1[val] = 1
total = 0
values = []
for key, value in dict1.iteritems(): #iterate through items in dict1
    if len(key) == 1: # if not it's a non-printable we've gone thru
        total += value
        values.append(value)
        dict1[key] = str(value) # convert value to string for JSON output
        if ord(key) > 32:
            key = key
        else:
            dict1[str(hex(ord(key)))] = dict1[key]
            del dict1[key]
dict1['total'] = str(total)
entropy = 0
for a in range(len(values)): # iterate thru array, summation entropy calculations
    values[a] = (values[a]/float(total))
    values[a] = (values[a] * math.log(values[a], 2))
    entropy += values[a]
entropy_dict = {}
entropy_dict['entropy'] = str(-entropy)
print json.dumps(dict1, sort_keys=True, indent=4, separators=(',',': ')) # for pretty JSON output
print json.dumps(entropy_dict, sort_keys=True, indent=4, separators=(',',': '))
