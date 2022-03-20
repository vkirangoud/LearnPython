name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

prolific = dict()
for line in handle:
    line.rstrip()
    # if  line.find('From ') == -1:
     #   continue
    if not line.startswith('From '): continue
    words = line.split()
    fr = words[1]
    prolific[fr] = prolific.get(fr,0) + 1

print(prolific)
hf = max(prolific.values()) # max value
for key in prolific:
    if prolific[key] == hf:
        print(key, hf)
        break





