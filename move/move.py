import time
import numpy as np
# import pyautogui
import win32api, win32con # install via: conda install pywin32

def move_mouse():
    # BASE_POSITION = 10
    # rand_x = np.random.randint(0, 800)
    # rand_y = np.random.randint(0, 600)
    # move_time = np.random.uniform(0.5, 2)
    # pyautogui.moveTo(BASE_POSITION + rand_x, BASE_POSITION + rand_y, duration=move_time)
    # x = BASE_POSITION + rand_x
    # y = BASE_POSITION + rand_y
    win32api.SetCursorPos((np.random.randint(100, 500), np.random.randint(100, 500)))
    time.sleep(3)
    x = 160
    y = 600
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print("Clicked at: ", x, y)

while (True):
    move_mouse()
    i = 0
    i_total = np.random.uniform(10, 20)
    while (i < i_total):
        time.sleep(1)
        i += 1
        print("Waiting for: ", i, " seconds out of ", i_total)
