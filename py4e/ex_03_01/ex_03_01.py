sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
print(type(sh))
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fr > 40 :
    print("Overtime")
else :
    print("Regular")
xp = fh * fr
print("Pay:", xp)
