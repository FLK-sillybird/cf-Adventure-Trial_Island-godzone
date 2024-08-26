import pyautogui
screenWidth, screenHeight = pyautogui.size()
# BLOOD 960000
import time
def hanshuang(times):
    for i in range(times):
        time.sleep(1)
        pyautogui.press('e')
        pyautogui.click(265, 410)
        pyautogui.click(815, 568)
        pyautogui.rightClick(350, 410)
        time.sleep(1)
        pyautogui.rightClick(350, 410)
        time.sleep(4)
        pyautogui.mouseDown(x=960,y=540)
        time.sleep(3)
        pyautogui.mouseUp()
        


