import time
import pydirectinput as auto
from pynput import keyboard
import win32gui
import win32con
def action(number,sleep_times,click_positions,star_key):    
    current_summon_count = 0
    global running  # 声明 running 为全局变量
    running = True
    # 启动键盘监听器
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # 启动后台线程
    hwnd = win32gui.FindWindow(None, '穿越火线')
    activate_window(hwnd)
    
    while current_summon_count < number and running:
        auto.press('e')
        if star_key == "one_star":
        
            auto.click(click_positions['1star']['x'], click_positions['1star']['y'])
            
        else:
            auto.click(click_positions['2star']['x'], click_positions['1star']['y'])
            
        auto.click(click_positions['card']['x'], click_positions['card']['y'])
        auto.click(click_positions['confirm']['x'], click_positions['confirm']['y'])
        
        #换子弹
        auto.press('r')
        time.sleep(sleep_times['cartridge_change_time'])
        
        time.sleep(sleep_times['waitForDuration'])
        auto.mouseDown()
        
        time.sleep(sleep_times['time2kill'])
        
        auto.mouseUp()

        time.sleep(sleep_times['waitTime'])

        current_summon_count += 1
    # 停止键盘监听器
    listener.stop()
    if running == True:
        return current_summon_count
    else:
        return current_summon_count-1

def activate_window(hwnd):
    if hwnd == 0:
        raise Exception("游戏窗口未找到")
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    except pywintypes.error as e:
        if e.winerror == 1400:
            raise Exception("游戏窗口句柄无效") from e
        raise
    win32gui.SetActiveWindow(hwnd)


def on_press(key):
    try:
        if key.char == 'q':  # 检查按下的键是否为 'q'
            global running  # 使用全局变量来控制循环
            running = False
    except AttributeError:
        pass  # 如果按键没有 char 属性，比如功能键，就忽略它