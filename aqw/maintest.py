# pip install pyautogui to make the code work
import pyautogui
import time
#import keyboard



time.sleep(5)




print('click on the game you have 5sec')
time.sleep(5)
print('Starting Upp')
time.sleep(0)
print('Online....')




def auto_start():
    #pyautogui.leftClick(x=1622, y=399)
    time.sleep(1)
    pyautogui.press(['1'])
    time.sleep(1)
    pyautogui.press(['2'])
    time.sleep(1)
    pyautogui.press(['3'])
    time.sleep(3)
    pyautogui.press(['4'])
    time.sleep(1)
    pyautogui.press(['5'])
    time.sleep(1)
   # pyautogui.press(['esc'])
    print('In Progress....')



while True:
    auto_start()

while False:
    exit()