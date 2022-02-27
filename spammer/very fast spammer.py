# this can break thing
import threading
import pyautogui
import time

time.sleep(5)
pyautogui.FAILSAFE = True



def spam1():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam2():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam3():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')


def spam4():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam5():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam6():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam7():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam8():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam9():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

def spam10():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

th1 = threading.Thread(target=spam1)
th1.start()
time.sleep(0.2)


th2 = threading.Thread(target=spam2)
th2.start()
time.sleep(0.2)

th3 = threading.Thread(target=spam3)
th3.start()
time.sleep(0.2)

th4 = threading.Thread(target=spam4)
th4.start()
time.sleep(0.2)

th5 = threading.Thread(target=spam5)
th5.start()
time.sleep(0.2)

th6 = threading.Thread(target=spam6)
th6.start()
time.sleep(0.2)

th7 = threading.Thread(target=spam7)
th7.start()
time.sleep(0.2)

th8 = threading.Thread(target=spam8)
th8.start()
time.sleep(0.2)

th9= threading.Thread(target=spam9)
th9.start()
time.sleep(0.2)

th10 = threading.Thread(target=spam10)
th10.start()
time.sleep(0.2)