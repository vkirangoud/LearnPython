name = input("Enter filename: ")
if (len(name) < 1): 
    name = "mbox-short.txt"
handle = open(name)
hrs = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    timestr = words[5].split(":")
    hr = timestr[0]
    hrs[hr] = hrs.get(hr, 0) + 1

lst = list()
for key, val in list(hrs.items()):
    lst.append((val,key))
lst.sort(reverse=True)

for val, key in lst:
    print(key, val)


    