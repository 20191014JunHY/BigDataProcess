import sys
file = sys.argv[1]
output = sys.argv[2]
f = open(file, "rt")
gdict = dict()
while True:
    txt = f.readline()
    if len(txt) == 0: break
    arr = txt.split("::")
    garr = arr[2].split("|")
    for g in garr:
        if g.strip() not in gdict:
            gdict[g.strip()] = 0
        else:
            gdict[g.strip()] += 1
f.close()
f = open(output, "wt")
keyList = list(gdict.keys())
for key in keyList:
    f.write(key + " " + str(gdict[key]) + "\n")
f.close()
