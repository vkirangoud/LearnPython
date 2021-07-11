sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit() #quit also works
 
print(fh, fr)
if fr > 40 :
    print("Overtime")
else :
    print("Regular")
xp = fh * fr
print("Pay:", xp)
