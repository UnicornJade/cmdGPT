import pyautogui
import time

time.sleep(2)
pyautogui.hotkey('command', 'space', interval=0.1)
time.sleep(2)
pyautogui.typewrite('Sublime Text', interval=0.1)
time.sleep(2)
pyautogui.press('return')
time.sleep(5)
pyautogui.typewrite('print("Hello world!")', interval=0.1)
time.sleep(2)
pyautogui.hotkey('command', 's', interval=0.1)
time.sleep(2)
pyautogui.typewrite('hello_world.py', interval=0.1)
time.sleep(2)
pyautogui.press('return')