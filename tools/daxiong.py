# BLOOD 730000

import pyautogui
import time

def daxiong(summon_count):
    current_summon_count = 0

    while current_summon_count < summon_count:
        time.sleep(1)
        pyautogui.press('e')
        pyautogui.click(350, 410)  #350
        pyautogui.click(815, 568)
        #击杀boss
        time.sleep(4)
        pyautogui.mouseDown(x=960,y=540,button='left')
        time.sleep(3)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.press('enter')
        #换子弹
        pyautogui.rightClick(350, 410)
        time.sleep(1)
        pyautogui.rightClick(350, 410)
        current_summon_count += 1