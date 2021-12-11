# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try: 
    fh = open(fname)
except:
    print('File not found.', fname)
    exit()
avg = 0.0
cnt = 0
for line in fh:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos =  line.find(':')
    avg +=  float(line[pos+1:])
    cnt += 1
print("Average spam confidence:", (avg)/cnt)
