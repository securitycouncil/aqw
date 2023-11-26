import pyautogui
import time
import keyboard
import pyfiglet

def pause_now():
    print('Pause')
    start_time = time.time()
    
    while not keyboard.is_pressed('r'):
        if keyboard.is_pressed('q'):
            exit_now()
            
        time.sleep(0.1)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f'Resuming... (Paused for {duration:.2f} seconds)')
    auto_start()

def exit_now():
    print('Exiting...')
    exit()

def auto_start():
    while True:
        
        if keyboard.is_pressed('p'):
            pause_now()

        if keyboard.is_pressed('q'):
            exit_now()

        time.sleep(1)
        pyautogui.press(['1'])

        if keyboard.is_pressed('p'):
            pause_now()

        if keyboard.is_pressed('q'):
            exit_now()

        time.sleep(1)

        pyautogui.press(['2'])
        time.sleep(1)

        if keyboard.is_pressed('p'):
            pause_now()

        if keyboard.is_pressed('q'):
            exit_now()

        time.sleep(1) 

        pyautogui.press(['3'])
        time.sleep(1)

        if keyboard.is_pressed('p'):
            pause_now()

        if keyboard.is_pressed('q'):
            exit_now()

        time.sleep(1) 

        # pyautogui.press(['4'])
        # time.sleep(1)

        if keyboard.is_pressed('p'):
            pause_now()

        if keyboard.is_pressed('q'):
            exit_now()

        time.sleep(1) 

        # pyautogui.press(['5'])
        print('In Progress....')
        time.sleep(1)

        if keyboard.is_pressed('p'):
            pause_now()

        if keyboard.is_pressed('q'):
            exit_now()




def start_pogram():
    # Initial delay to allow the user to click on the game
    print('Click on the game you have 5 seconds...')
    time.sleep(5)

    print('Starting Upp')
    time.sleep(1)
    print('Online....')
    auto_start()

def pause_the_app():
    pause_now()

def exit_the_pogram():
    exit_now()




text = "Welcome to AQW Auto Clicker"
ascii_art = pyfiglet.figlet_format(text)

print(ascii_art)
print("""
If you press:
  1 - Start the program
  2 - Pause the program
  3 - Exit the program
  4 - Non-option chosen. Exiting program    
""")
# Prompt the user to pick 1, 2, or 3
user_choice = input("Enter 1, 2, or 3: ")

# Check the user's input and call the corresponding function
if user_choice == "1":
    start_pogram()
elif user_choice == "2":
    pause_the_app()
elif user_choice == "3":
    exit_the_pogram()
else:
    print("Invalid choice. Non-option chosen. Exiting program")
    exit_now()



# Infinite loop for continuous execution
while True:
    auto_start()
