import pyautogui #mouse jiggles until stopped with CRT C

import time

#End mouse jiggling with CRT+C

userInput = input("What to say: ")
while userInput == "yes":
  
   pyautogui.moveRel(5,0, duration =0.1)
   pyautogui.moveRel(-5,0, duration =0.1)
   time.sleep(2)