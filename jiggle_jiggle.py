import pyautogui

# pyautogui.displayMousePosition() # Live mouse position (changing)

print(pyautogui.position()) # Prints current mouse position (non-changing)

print(pyautogui.size()) #prints size of main screen, width height

print(pyautogui.onScreen(48000, 2)) 