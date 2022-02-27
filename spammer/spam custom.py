import pyautogui
import time
time.sleep(5)
pyautogui.FAILSAFE = True

while True:
    print('sending')
    pyautogui.typewrite('HAPPY BIRTHDAY')
    pyautogui.press('enter')



