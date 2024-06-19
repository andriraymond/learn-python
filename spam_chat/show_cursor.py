import pyautogui
import time 

num = 1

# Create a while function to repeat the function and display the cursor position
while num != 0:
    current_position = pyautogui.position()
    print(f"Cursor position : {current_position}")
    time.sleep(5)       # sleep for 5 seconds to display the cursor position
