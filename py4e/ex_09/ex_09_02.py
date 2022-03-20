import string
fname = input('Enter the file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
counts = dict()
for line in fh:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print(counts)
