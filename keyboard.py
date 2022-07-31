from time import sleep
import pyautogui
import sys
def PasswordStroker(password):
    print(password)
    sleep(2)
    for i in password:
        if i=="\"" or i=="!" or i=="{" or i=="}" or i=="&" or i=="~" or i==">" or i=="<" or i=="$" or i=="@" or i=="#" or i=="%" or i=="^" or i=="*" or i=="(" or i==")" or i=="_" or i=="+" or i==":"or i=="|"or i=="?":
            pyautogui.keyDown("shift")
            pyautogui.press(i)
            pyautogui.keyUp("shift")
        elif(ord(i)>=65 and ord(i)<=90):
            pyautogui.keyDown("shift")
            pyautogui.press(i)
            pyautogui.keyUp("shift")
        else:
            pyautogui.press(i)
    pyautogui.press("enter")
if __name__ == "__main__":
    PasswordStroker(sys.argv[1])
