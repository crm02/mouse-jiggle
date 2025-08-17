import pyautogui #mouse jiggles for x amount of seconds

import time



print(time.time())
start_time = time.time()
duration = int(input("How long would you like to jiggle?: "))
end_time = start_time + duration

def jiggleMouse(end_time):
    while time.time() < end_time:
        pyautogui.moveRel(5,0, duration =0.1)
        pyautogui.moveRel(-5,0, duration =0.1)
        time.sleep(2)
    print('done')
    
jiggleMouse(end_time)
