import pyautogui, time


f = open("messages.txt", "r")
for word in f:
    time.sleep(2)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
