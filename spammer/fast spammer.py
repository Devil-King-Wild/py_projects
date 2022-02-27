import threading
import pyautogui
import time
import keyboard
time.sleep(5)
pyautogui.FAILSAFE = True


def spam1():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY')


def spam2():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY')


th1 = threading.Thread(target=spam1)
th1.start()
time.sleep(0.2)


th2 = threading.Thread(target=spam2)
th2.start()