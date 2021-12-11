
mini = None
maxi = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        val = int(sval)
    except:
        print('Invalid input')
        continue
    if mini is None or mini > val:
        mini = val
    if maxi is None or maxi < val:
        maxi = val

print('Maximum is', maxi)
print('Minimum is', mini)
