import time
import numpy as np
# import pyautogui
import win32api, win32con # install via: conda install pywin32

print("\n\nStart time: ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
start = time.time()

RIGHT_SCREEN_OFFSET = 1920 # 0 or 1920 depending on the screen

def move_mouse():
    # BASE_POSITION = 10
    # rand_x = np.random.randint(0, 800)
    # rand_y = np.random.randint(0, 600)
    # move_time = np.random.uniform(0.5, 2)
    # pyautogui.moveTo(BASE_POSITION + rand_x, BASE_POSITION + rand_y, duration=move_time)
    # x = BASE_POSITION + rand_x
    # y = BASE_POSITION + rand_y
    win32api.SetCursorPos((np.random.randint(200 + RIGHT_SCREEN_OFFSET, 300 + RIGHT_SCREEN_OFFSET),
                           np.random.randint(100, 500)))
    time.sleep(1)
    x = 100 + RIGHT_SCREEN_OFFSET
    y = 600
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print("Clicked at: ", x, y)

total_min = 30000
while (time.time() - start < total_min*60):
    print("\n" + "*"*10 + " Time elapsed (min):", int((time.time() - start)/60),
          "out of", total_min, "minutes" + "\n")
    move_mouse()
    i = 0
    i_total = int(np.random.uniform(20, 30))
    while (i < i_total):
        time.sleep(2)
        print("Waiting for:", i, "out of", i_total, "seconds")
        i += 2

print("End time: ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
