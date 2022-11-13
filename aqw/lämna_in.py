import pyautogui
import time

start = input("press y to start and n for exit\n")





print('click on the game you have 10 sec')
time.sleep(10)
print('Starting Upp')
time.sleep(0)
print('Online....')

def good_shit():
    pyautogui.leftClick(x=5364, y=396)
    time.sleep(2)
    pyautogui.leftClick(x=5529, y=828)
    time.sleep(2)
    pyautogui.leftClick(x=5402, y=827)
    print("testar ingen om 30 sec")
    time.sleep(30)

while True:
    good_shit()