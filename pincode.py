import random
import pyautogui

char = "1234567890"
lis = list(char)
pwd = pyautogui.password("enter a password")
sample = ""
while "".join(sample) != pwd:
    sample = random.choices(lis,k=len(pwd))
    print(sample)
    if sample == list(pwd):
        print("your pass word is ", "".join(sample))
        break