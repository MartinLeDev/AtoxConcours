from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key, Listener
import time
from random import *

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R", "S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

keyboard = KeyboardController()
mouse = MouseController()


Run = True
generatedCode = int(input("Combien de code à tester ?"))

def Launch():
    writeFile = open('code.txt', "a+")
    time.sleep(0.25)
    press = True
    # Mouse to coordinate of button "enter your code" (922, 836)
    while press:
        mouse.position = (922, 836)
        mouse.press(Button.left)
        mouse.release(Button.left)
        press = False

    # Mouse to coordinate of entry "enter your code"
    mouse.position = (841, 636)
    time.sleep(0.05)
    mouse.press(Button.left)
    mouse.release(Button.left)
    code = "";
    # Enter the code
    writeFile.write(str("\n"))
    for y in range(5):
        time.sleep(0.05)
        for i in range(4):
            randomChar = None
            if i != 3:
                randomChar = letters[randint(0, len(letters) - 1)]
            else:
                randomChar = numbers[randint(0, len(numbers) - 1)]
            keyboard.press(randomChar)
            keyboard.release(randomChar)
            code += randomChar;
        code += "-";

    writeFile.write(str(code))
    # Valider le code
    mouse.position = (1064, 716)
    time.sleep(0.05)
    mouse.press(Button.left)
    mouse.release(Button.left)


    writeFile.close()
    time.sleep(1)
    print(code)
    global generatedCode

    generatedCode = generatedCode - 1
    Run = inverse(generatedCode == 0)

    if Run:
        mouse.position = (922, 836)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
        Launch()

def inverse(bool):
    if bool:
        return False
    else:
        return True
def main():
    Launch()

if __name__ == "__main__":
    main()
