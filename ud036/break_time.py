import webbrowser
import time
loop = 0
time.ctime() # prints current time
while loop < 3:
    time.sleep(10)
    webbrowser.open("http://www.gmail.com")
    loop = loop + 1

