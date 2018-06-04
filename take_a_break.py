import time
import webbrowser

count = 0

print("The Program start on"+time.ctime())
while(count < 9):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=UT_WZpZyF2M")
    count = count + 1 
