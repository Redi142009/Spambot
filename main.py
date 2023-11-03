import pyautogui
import time

def Spambot():
    x = 0
    for i in range(5):
        x += 1
        print(x)
        time.sleep(1)
        if x == 5:
            for q in range(50):
                pyautogui.write("Kamu nanyea?")
                pyautogui.press("Enter")
                time.sleep(0.5)

Spambot()