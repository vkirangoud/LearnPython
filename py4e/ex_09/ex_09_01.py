# dictionary
try:
    fh = open('words.txt')
except:
    print('words.txt file not found');
    exit()
histg = dict()
for line in fh:
    words = line.split()
    for word in words:
        if word in histg:
            histg[word] += 1
        else:
            histg[word] = 1

lst = list(histg.keys())
lst.sort()
for key in lst:
    print(key, histg[key])

