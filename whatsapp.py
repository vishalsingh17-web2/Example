import pyautogui as pt
import time
limit = 100
time.sleep(1)
message = "Ye mai nahi kr rAHA"
for i in range(200):
    pt.typewrite(message)
    pt.press("enter")
    
