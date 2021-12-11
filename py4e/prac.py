import math

print(math)

print('Spam ' + '4');
math.sqrt(5)

fruit = 'banana'
idx = len(fruit) - 1

while idx >= 0 :
    letter = fruit[idx]
    print(letter)
    idx = idx - 1

for char in fruit:
    print(char)

print(fruit[:])
#fruit[0] = 'H' # reports error - strings are immutable 

def freq(str, let):
    cnt = 0
    for x in str:
        if x == let:
            cnt += 1
    print(cnt)
    return cnt

print(freq(fruit,'a'))

print('x' in fruit)
print('a' in fruit)

dir(fruit)

camels = 42
str = 'I have spotted %d camels' % camels
print(str)

fhand = open('output.txt', 'w')
print(fhand)
fhand.write(str)
line2 = '\nI know that dude.\n'
fhand.write(line2)
fhand.close()

fh = open('mbox-short.txt')
for line in fh:
    if not line.startswith('From') : continue
    lst = ()
    lst = line.split()
    print(lst[1])
    