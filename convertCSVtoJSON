import simplejson as json
import os

fileStr='/Users/walkerrowe/Documents/imdb/100.basics.tsv'
f = open(fileStr, 'r')
o = open('/Users/walkerrowe/Documents/imdb/100.basics.json', 'w')


def formatJSON(l, cols):
    json = {}

    for i in range(len(l)):
        json[cols[i]] = {"S": l[i]}

    return json


cols = []



i = 0
filePos=0
f.seek(0, os.SEEK_END)
f.seek(0)

for l in f:
    ln = l.strip("\\N").strip("\n")
    filePos = filePos + len(l)
    f.seek(filePos)
    line = ln.split('\t')
    if i == 0:
        i = 1
        cols = line
    else:
        if filePos < os.stat(fileStr).st_size:
            str = json.dumps(formatJSON(line, cols)) + '},\n'
            o.write(json.dumps(formatJSON(line, cols)) + '},\n')
        else:
            str = json.dumps(formatJSON(line, cols)) + '\n'
            o.write(str)



o.close()
