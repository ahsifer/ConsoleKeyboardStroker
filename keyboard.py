from time import sleep
import pyautogui
import sys
def PasswordStroker(password):
    sleep(2)
    for i in password:
        if(ord(i)>=65 and ord(i)<=90):
            pyautogui.keyDown("shift")
            pyautogui.press("{}".format(i))
            pyautogui.keyUp("shift")
        else:
            pyautogui.press("{}".format(i))
    pyautogui.press("enter")
if __name__ == "__main__":
    PasswordStroker("{}".format(sys.argv[1]))
