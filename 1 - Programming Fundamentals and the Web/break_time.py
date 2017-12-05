import webbrowser
import time
breaks = 0

while breaks < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=4fndeDfaWCg")
    breaks = breaks+1
    print "break = ", breaks
print "done"
