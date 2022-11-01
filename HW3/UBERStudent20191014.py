import datetime
import sys
file = sys.argv[1]
output = sys.argv[2]
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
f = open(file, "rt")
rvdict = dict()
rtdict = dict()
while True:
    txt = f.readline()
    if len(txt) == 0: break
    arr = txt.split(",")
    dt_datetime = datetime.datetime.strptime(arr[1],"%m/%d/%Y")
    day = days[datetime.date(dt_datetime.year, dt_datetime.month, dt_datetime.day).weekday()]
    key = arr[0] + ',' + day
    if key not in rvdict:
        rvdict[key] = 0
        rtdict[key] = 0
    else:
        rvdict[key] += int(arr[2])
        rtdict[key] += int(arr[3])
f.close()
f = open(output, "wt")
keyList = list(rvdict.keys())
for key in keyList:
    f.write(key + " " + str(rvdict[key]) + "," + str(rtdict[key]) + "\n")
f.close()