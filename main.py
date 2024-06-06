import pyautogui
import time
import pygetwindow as gw
import keyboard

pyautogui.FAILSAFE = False

def perform_action(img_path):
    text_location = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.8)
    if text_location:
        x, y = pyautogui.center(text_location)
        pyautogui.moveTo(x, y)
        pyautogui.click()

def wait_and_click(interval=0):
    perform_action("decant.png")
    perform_action("decant 2.png")
    time.sleep(interval)

def activate_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        window.activate()
        return window
    return None

def move_and_click(window, rel_x, rel_y):
    abs_x = window.left + rel_x
    abs_y = window.top + rel_y
    pyautogui.moveTo(abs_x, abs_y)
    pyautogui.click()

def main():
    window = activate_window('League of Legends')
    if window:
        while not keyboard.is_pressed('F1'):
            time.sleep(1)
            move_and_click(window, 100, 200)
            wait_and_click(interval=0.5)
    else:
        print("League of Legends window not found.")

if __name__ == "__main__":
    main()
