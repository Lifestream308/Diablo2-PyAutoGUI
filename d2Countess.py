import pyautogui
import time
import d2Functions

# Shift + Window button + S key will allow me to make screenshot of certain area I choose


screen_width, screen_height = pyautogui.size()

# find d2 icon on bottom screen, click on icon
d2Functions.findD2Icon()

time.sleep(1)

# find Poison pic to select character on right screen, double click, wait 
d2Functions.findPoisonName()

time.sleep(1)

# find Hell pic, click, wait for load
image_path = 'diablo2Images/hellDifficulty.jpg'
region = (screen_width * 2 // 5, screen_height * 2 // 5, screen_width // 5, screen_height // 5)
location = pyautogui.locateOnScreen(image_path, confidence=0.8, region=region)

if location:
    print(f"Hell difficulty found at: {location}")
    pyautogui.click(x=location.left, y=location.top)
else:
    print("Printing out error: Hell difficulty image not found.")







# Should now be in act 1

# wait and check if loading screen finished, then click halfway to waypoint
time.sleep(15)
image_path = 'diablo2Images/angelArm.jpg'
region = (0, screen_height * 5 // 6, screen_width // 4, screen_height // 6)
location = pyautogui.locateOnScreen(image_path, confidence=0.8, region=region)

if location:
    print(f"Game loaded. Angel arm found at: {location}")
    pyautogui.click(x=1320, y=250)
else:
    print("Printing out error: Angel arm image not found.")
    time.sleep(5)
    pyautogui.click(x=1320, y=250)

time.sleep(0.8)

# click on waypoint
pyautogui.moveTo(856, 103, duration=1)
pyautogui.click()

time.sleep(1)

# search waypoint image screen on top, click black marsh
# not going to search, just going to start clicking for now

# click Black Marsh waypoint
pyautogui.click(x=366, y=515)

# wait for loading screen
time.sleep(3)

# select teleport spell
pyautogui.press('F5')

time.sleep(0.3)

# right click to teleport multiple times towards bottom left corner
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)
pyautogui.rightClick(x=103, y=1079)
time.sleep(0.27)

# right click teleport to the right into the tower
pyautogui.rightClick(x=1850, y=850)
time.sleep(0.27)
pyautogui.rightClick(x=1850, y=850)
time.sleep(0.27)
pyautogui.rightClick(x=1850, y=850)

# now inside tower ruins, move mouse to enter the ruins by clicking
pyautogui.moveTo(x=927, y=635, duration=1)
pyautogui.click()

time.sleep(3)
pyautogui.press('Esc')

# Check image to see if inside the safe part of the ruins. Unpause if safe
image_path = 'diablo2Images/safeRuins.jpg'
region = (0, 0, screen_width // 2, screen_height)
location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

if location:
    print(f"Safe. Ruins image found at: {location}")
    pyautogui.press('Esc')
else:
    print("Printing out error: Safe Ruins image not found.")

time.sleep(1)

# click on entrance to ruins officially
pyautogui.moveTo(545, 543, duration=1)
pyautogui.click()
time.sleep(2)

# right click teleport to right side of screen closer to level 2
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=950)
time.sleep(0.27)

# right click teleport to upper left side of screen to finish reaching level 2 entrance
pyautogui.rightClick(x=1919, y=1)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1)
time.sleep(0.27)

pyautogui.moveTo(920, 255, duration=0.75)
pyautogui.click()

time.sleep(0.5)

pyautogui.press('Esc')

# Check image to see if inside the safe part of ruins level 2. Unpause if safe
image_path = 'diablo2Images/ruinsLevel2.jpg'
region = (0, 0, screen_width // 2, screen_height)
location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

if location:
    print(f"Ruins level 2 image found at: {location}")
    pyautogui.press('Esc')
else:
    print("Printing out error: Safe Ruins image not found.")

time.sleep(10)

pyautogui.press('Esc')