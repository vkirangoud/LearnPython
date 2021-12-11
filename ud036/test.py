def countdown(n):
    if n == 0:
        return
    else:
        countdown(n-1)
        print (n)
        if n == 3:
            print("All Set Go !!!");
        
countdown(3)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print (factorial(3))
