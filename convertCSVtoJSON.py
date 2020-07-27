

import simplejson as json
import os

fileStr='/Users/walkerrowe/Documents/customers.csv'
f = open(fileStr, 'r')
o = open('/Users/walkerrowe/Documents/customers.json', 'w')


def formatJSON(l, cols):
    json = {}

    for i in range(len(l)):
        json[cols[i]] = l[i]

    return json


cols = []

def formatJSON(l, cols):
    json = {}

    for i in range(len(l)):
        json[cols[i]] = l[i]

    return json


cols = []



i = 0
filePos=0
f.seek(0)
o.write("[")

for l in f:
    filePos = filePos + len(l)
    f.seek(filePos)
    line = l.split(',')
    if i == 0:
        i = 1
        cols = line
    else:
        if filePos < os.stat(fileStr).st_size:
           o.write(json.dumps(formatJSON(line, cols)) + ',\n')
        else:
           o.write(json.dumps(formatJSON(line, cols)) + '\n')


o.write("]")

o.close()
