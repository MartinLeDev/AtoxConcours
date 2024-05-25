from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key, Listener
import time
from random import *
from PIL import Image, ImageChops
import pyautogui

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R", "S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

keyboard = KeyboardController()
mouse = MouseController()


Run = True


def capture_screen(screen_number=1):
    """
    Capture the specified screen.
    Note: This function assumes a setup where the screens are not mirrored and are side by side.
    """
    screens = pyautogui.screenshot().size  # Get the size of the screenshot (entire screen area)
    screen_width, screen_height = screens[0] // 2, screens[1]  # Assume two screens of equal width
    if screen_number == 1:
        left = 0
        top = 0
        right = screen_width
        bottom = screen_height
    elif screen_number == 2:
        left = screen_width
        top = 0
        right = screens[0]
        bottom = screen_height
    else:
        raise ValueError("Invalid screen number. Only screen 1 or 2 is supported.")

    return pyautogui.screenshot(region=(left, top, right - left, bottom - top))


def is_image_on_screen(image_path, screen_number=1):
    """
    Check if the given image is present on the specified screen.

    :param image_path: Path to the image file to check.
    :param screen_number: The screen number to capture and check.
    :return: True if the image is found on the screen, False otherwise.
    """
    screen = capture_screen(screen_number)
    screen = screen.convert('RGB')
    target_image = Image.open(image_path).convert('RGB')

    screen_width, screen_height = screen.size
    img_width, img_height = target_image.size

    for x in range(screen_width - img_width + 1):
        for y in range(screen_height - img_height + 1):
            box = (x, y, x + img_width, y + img_height)
            region = screen.crop(box)
            if ImageChops.difference(region, target_image).getbbox() is None:
                return True
    return False

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
    b = is_image_on_screen("ressource/img.png",1)
    print(code +"  :  "+b)

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
