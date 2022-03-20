import string
name = input("Enter file name: ")
if (len(name) < 1 ):
    name = "mbox.txt"
handle = open(name)
letters = dict()
for line in handle:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for alps in word:
            letters[alps] = letters.get(alps, 0) + 1

for key, val in list(letters.items()):
    print(key, val)

