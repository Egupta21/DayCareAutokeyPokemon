import pyautogui;
import time;

time.sleep(3)
for i in range(100):
    pyautogui.keyDown('s')
    time.sleep(4)
    pyautogui.keyUp('s')
    pyautogui.keyDown('w')
    time.sleep(4)
    pyautogui.keyUp('w')
    
