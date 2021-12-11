def computepay(h, r):
    if (h < 40):
        return h * r
    else:
        over40 = h - 40
        return 40*r + over40*r*1.5


hrs = input("Enter Hours:")
hrs = float(hrs)
r   = input("enter hourly rate:")
rate = float(r)
p = computepay(hrs, rate)
print("Pay", p)