fname = input("Enter file name: ")
try: 
    fh = open(fname)
except:
    print("File not exsits", fname)
    exit()
lst = list()
for line in fh:
    line = line.rstrip()
    lsa = line.split()
    for wrd in lsa:
        if wrd not in lst:
            lst.append(wrd)
    
lst.sort()
print(lst)