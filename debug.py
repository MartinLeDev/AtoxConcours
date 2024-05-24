from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Listener

mouse = MouseController()

def on_press(key):
    if key == Key.f6:
        print(f"Mouse position: {mouse.position}")

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
