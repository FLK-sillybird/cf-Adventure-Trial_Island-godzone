# BLOOD 730000
import pyautogui
import time
import keyboard
def juren(summon_count):
    current_summon_count = 0

    while current_summon_count < summon_count:
        time.sleep(1)
        pyautogui.press('e')
        pyautogui.click(265, 410)  
        pyautogui.click(815, 568)
        #击杀boss
        time.sleep(5)
        pyautogui.mouseDown(x=960,y=540,button='left')
        time.sleep(1)
        pyautogui.mouseUp(button='left')
        time.sleep(5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(3)
        #换子弹
        pyautogui.rightClick(350, 410)
        time.sleep(1)
        pyautogui.rightClick(350, 410)
        # time.sleep(3)
        current_summon_count += 1







