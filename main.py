from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key, Listener
import time
from random import *

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R", "S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

keyboard = KeyboardController()
mouse = MouseController()

writeFile = open('code.txt', "a+")

Run = True
def Launch():
    time.sleep(1)
    press = True
    # Mouse to coordinate of button "enter your code" (922, 836)
    while press:
        time.sleep(0.1)
        mouse.position = (922, 836)
        mouse.press(Button.left)
        mouse.release(Button.left)
        press = False

    # Mouse to coordinate of entry "enter your code"
    mouse.position = (841, 636)
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)

    # Enter the code
    writeFile.write("/n")
    for y in range(5):
        time.sleep(0.1)
        for i in range(4):
            randomChar = None
            if i != 3:
                randomChar = letters[randint(0, len(letters) - 1)]
            else:
                randomChar = numbers[randint(0, len(numbers) - 1)]
            keyboard.press(randomChar)
            keyboard.release(randomChar)
            writeFile.write(randomChar)
        writeFile.write("-")

    # Valider le code
    mouse.position = (1064, 716)
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(1)
    if Run:
        mouse.position = (922, 836)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)

def on_press(key):

    if key == Key.f6:
        Run = False
    if key == Key.f5:
        Run = True
        Launch()

def inverse(bool):
    if bool == True:
        return False
    else:
        return True
def main():
    if inverse(Run):
        exit()
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
