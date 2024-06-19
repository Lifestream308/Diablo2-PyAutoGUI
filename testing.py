import pyautogui
import time

# Wait for 2 seconds before starting
time.sleep(1)

# Print the current mouse position
print(pyautogui.position())

time.sleep(1)

print(pyautogui.position())

time.sleep(1)

print(pyautogui.position())

# screen_width, screen_height = pyautogui.size()
# try:
#     image_path = 'diablo2Images/loot/lemRune.jpg'
#     region = (0, 0, screen_width, screen_height)
#     location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)
#     if location:
#         print(f"Lem Rune image found at: {location}")
#     pyautogui.moveTo(location.left + 10, location.top + 10, duration=0.6)
#     pyautogui.click()

# except Exception as e:
#     print(f"Error. Can't find level 5 Entrance: {e}")