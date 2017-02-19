import json
f = open("spectrum.json","r")
items = []
for line in f:
    item = line.split(':')[0][1:-1]
    items.append(item)
o = open("out.txt","w")
o.write(json.dumps(items[1:-1]))