name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
prolific = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    fr = words[1]
    prolific[fr] = prolific.get(fr, 0) + 1

lst = list()
for key, val in list(prolific.items()) :
    lst.append((val,key))
lst.sort(reverse=True)
val, key = lst[0]
print(key, val)
