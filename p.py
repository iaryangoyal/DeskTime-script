import pyautogui
import time
import random

def click_within_rectangle(top_left, bottom_right, interval):
    while True:  
        x = random.randint(top_left[0], bottom_right[0])
        y = random.randint(top_left[1], bottom_right[1])
        pyautogui.click(x, y)
        time.sleep(interval)

if __name__ == "__main__":
    top_left = (75, 250) 
    bottom_right = (150, 800)  
    
    click_within_rectangle(top_left, bottom_right, interval=5) # seconds

    # make sure you open it in vscode explorer and run it in the terminal