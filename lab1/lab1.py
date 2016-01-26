import json
import math
import sys

dict1 = {}
with open(str(sys.argv[1]), 'rb') as textFile:
    for line in textFile:
        chars = list(unicode(line, errors='ignore'))
        for val in chars:
            if val in dict1:
                dict1[val] += 1
            else:
                dict1[val] = 1
total = 0
values = []
for key, value in dict1.iteritems():
    if len(key) == 1:
        total += value
        values.append(value)
        dict1[key] = str(value)
        if ord(key) > 32:
            key = key
        else:
            dict1[str(hex(ord(key)))] = dict1[key]
            del dict1[key]
dict1['total'] = str(total)
entropy = 0
for a in range(len(values)):
    values[a] = (values[a]/float(total))
    values[a] = (values[a] * math.log(values[a], 2))
    entropy += values[a]
entropy_dict = {}
entropy_dict['entropy'] = str(-entropy)
print json.dumps(dict1, sort_keys=True, indent=4, separators=(',',': '))
print json.dumps(entropy_dict, sort_keys=True, indent=4, separators=(',',': '))
