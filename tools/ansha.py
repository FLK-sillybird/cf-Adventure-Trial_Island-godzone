import pyautogui
import time

# BLOOD 780000

def ansha(summon_count):
    current_summon_count = 0

    while current_summon_count < summon_count:
        time.sleep(1)
        pyautogui.press('e')
        pyautogui.click(265, 410)
        pyautogui.click(815, 568)
        #击杀boss
        time.sleep(5)
        pyautogui.mouseDown(x=960,y=540,button='left')
        time.sleep(5)   #一星  3.5
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        #换子弹
        pyautogui.rightClick(350, 410)
        time.sleep(1)
        pyautogui.rightClick(350, 410)
        current_summon_count += 1
        


