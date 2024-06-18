import pyautogui
import time

# Wait for 2 seconds before starting
time.sleep(1)

# Move the mouse to position (100, 100)
# pyautogui.moveTo(100, 100, duration=1)

# Click the left mouse button
# pyautogui.click()

# Type a message
# pyautogui.write('Hello, PyAutoGUI!', interval=0.1)

# Press the Enter key
# pyautogui.press('enter')

# Press the F5 key
# pyautogui.press('F5')

# Perform a right-click at the current mouse position
# pyautogui.rightClick()

# Alternatively, you can right-click at a specific position directly
# pyautogui.rightClick(x=200, y=200)

# Print the current mouse position
print(pyautogui.position())

time.sleep(1)

print(pyautogui.position())

time.sleep(1)

print(pyautogui.position())