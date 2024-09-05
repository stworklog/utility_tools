import time
import numpy as np
import pyautogui

def move_mouse():
    BASE_PAUSE = 2
    BASE = 10
    rand_x = np.random.randint(0, 1000)
    rand_y = np.random.randint(0, 600)
    move_time = np.random.uniform(0.5, 2)
    pyautogui.moveTo(BASE + rand_x, BASE + rand_y, duration=move_time)
    print("Moved")
    pause_duration = BASE_PAUSE + np.random.uniform(0, 10)
    time.sleep(pause_duration)

while (True):
    move_mouse()
