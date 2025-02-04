import pyautogui
import time
import keyboard


def autoclicker(interval=2, toggle_key='f'):
    print(f"Натисніть '{toggle_key}' для запуску/зупинки...")
    running = False
    base_x, base_y = pyautogui.position()
    offset_y = 50
    offset_x = 0

    while True:
        if keyboard.is_pressed(toggle_key):
            base_x, base_y = pyautogui.position()
            running = not running
            print("Автоклікер запущено" if running else "Автоклікер зупинено")
            # Запобігання багаторазовому спрацюванню на одне натискання
            time.sleep(0.5)

        if running:
            pyautogui.click(base_x, base_y)
            time.sleep(interval)
            pyautogui.click(base_x + offset_x, base_y + offset_y)
            time.sleep(interval)


autoclicker()
