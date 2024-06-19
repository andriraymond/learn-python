import pyautogui
import time

print("Initial code... wait for 5 seconds...")
print("Please open your chat window")

time.sleep(5)                           # wait for 5 seconds to open the chat application

num = 2                                 # number of looping, change as desired for example I want to loop chat 50 times

for i in range(num):

    pyautogui.moveTo(560, 698)          # Change the position of the chat column
    pyautogui.write("Hello, world!")
    time.sleep(0.1)                     
    pyautogui.press('Enter')
    print(f"Passes {i + 1} {'times'}")  # print the number of times
    time.sleep(0.5)                     # sleep for a second, change as desired