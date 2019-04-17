import os
import json

paths = []
notebooks = []
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".ipynb"):
            paths.append(os.path.join(root, file))

for path in paths:
    myFile = open(path, "r")
    nbInfo = json.loads(myFile.read())
    nbInfo = nbInfo["metadata"]
    try:
        nbInfo = nbInfo["notebookInfo"]
        notebooks.append(json.dumps(nbInfo))
    except:
        continue

wFile = open("data.json", "w+")
wFile.write("{")
for i, x in enumerate(notebooks):
    index = '"' + str(i) + '" : '
    # print(index)
    wFile.write(index)
    wFile.write(x)
    if i != len(notebooks) - 1 :
        wFile.write(",")
wFile.write("}")
wFile.close()
# print(myFile.read())