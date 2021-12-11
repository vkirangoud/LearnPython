fhand = open('mbox-short.txt')
for line in fhand:
    line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
fname = input('Enter file name > ')
try: 
    fhand = open(fname)
except:
    print('File cannot be opened ', fname )
    exit()
for line in fhand:
    line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line.upper())