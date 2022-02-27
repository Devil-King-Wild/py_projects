import time
import pyautogui
import schedule
import time
time.sleep(5)
pyautogui.FAILSAFE = True



def job():
    while True:
        print('sending')
        pyautogui.typewrite('HAPPY BIRTHDAY')
        pyautogui.press('enter')

schedule.every().day.at('23:59').do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)