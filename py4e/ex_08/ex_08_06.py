lst = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    try:
        val = float(inp)
    except:
        print('Enter number only')
        continue
    lst.append(val)

print('Maximum: ', max(lst))
print('Minimum: ', min(lst))