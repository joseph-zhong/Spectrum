import json

names = open("Google-News.txt", "r")
titles = []
theLine  = names.readline()
theLine = names.readline()
for line in names:
    items = line.split()
    if len(items) == 2:
        lang = items[0]
        title = items[1]
        if lang == "ENGLISH":
            titles.append(title)
out = open("sites.json", "w")
out.write(json.dumps(titles))