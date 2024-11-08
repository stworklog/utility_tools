import time
import numpy as np
# import pyautogui
import win32api, win32con # install via: conda install pywin32

print('\n\nStart time: ',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
start = time.time()

RIGHT_SCREEN_OFFSET = 1920 # 0 or 1920 depending on the screen

def move_mouse():
    win32api.SetCursorPos((np.random.randint(200 + RIGHT_SCREEN_OFFSET, 300 + RIGHT_SCREEN_OFFSET),
                           np.random.randint(100, 500)))
    time.sleep(1)
    x = 100 + RIGHT_SCREEN_OFFSET
    y = 600
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print('Clicked at: ', x, y)

total_min = 30000

try:
    while (time.time() - start < total_min*60):
        print('\n' + '*'*10 + ' Time elapsed (min):', int((time.time() - start)/60),
            'out of', total_min, 'minutes' + '\n')
        move_mouse()
        elapsed_time = 0
        i_total = int(np.random.uniform(20, 30))
        sleep_time_step = 2
        while (elapsed_time < i_total):
            time.sleep(sleep_time_step)
            print('Waiting for:', elapsed_time, 'out of', i_total, 'seconds')
            elapsed_time += sleep_time_step

except KeyboardInterrupt:
    print('Starting time: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
    print('Ending time: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('Total elapsed time (min): ',  int((time.time() - start)/60))
