import pyautogui
import time
import d2Functions
import repeatCountessRun

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
time.sleep(11)
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
pyautogui.moveTo(856, 0, duration=.1)
pyautogui.moveTo(856, 103, duration=.5)
pyautogui.click()

time.sleep(1)

# click Black Marsh waypoint
pyautogui.click(x=366, y=515)

# wait for loading screen
time.sleep(2)

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

# right click teleport to the right into the tower. After 2 teleports, near water well. May want to add clicking water well
pyautogui.rightClick(x=1850, y=850)
time.sleep(0.27)
pyautogui.rightClick(x=1850, y=850)
time.sleep(0.27)
pyautogui.rightClick(x=1850, y=850)

# now inside tower ruins, move mouse to enter the ruins by clicking
pyautogui.moveTo(x=927, y=635, duration=.5)
pyautogui.click()

time.sleep(1.5)
pyautogui.press('Esc')

# Check image to see if inside the safe part of the ruins. Unpause if safe
image_path = 'diablo2Images/safeRuins2.jpg'
region = (0, 0, screen_width // 2, screen_height)
location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

if location:
    print(f"Safe. Ruins image found at: {location}")
    pyautogui.press('Esc')
else:
    print("Printing out error: Safe Ruins image not found.")

time.sleep(.5)

# click on entrance to ruins officially
pyautogui.moveTo(545, 543, duration=.5)
pyautogui.click()
time.sleep(.75)

# right click teleport to right side of screen closer to level 2
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1000)
time.sleep(0.27)

# right click teleport to upper left side of screen to finish reaching level 2 entrance
pyautogui.rightClick(x=1919, y=1)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1)
time.sleep(0.27)
pyautogui.rightClick(x=1919, y=1)
time.sleep(0.27)
pyautogui.rightClick(x=820, y=200)

# move mouse above entrance to level 2 ruins
pyautogui.moveTo(1054, 100, duration=0.15)

# manually click entrance for now, but soon try searching for image of entrance to level 2
try:
    image_path = 'diablo2Images/ruinsLevel2Entrance.jpg'
    region = (0, 0, screen_width, screen_height)
    location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)
    if location:
        print(f"Ruins level 2 ENTRANCE image found at: {location}")
    pyautogui.moveTo(location.left + 75, location.top + 100, duration=0.6)
    pyautogui.click()

except Exception as e:
    print(f"Error. Can't find level 2 Entrance: {e}")

time.sleep(0.5)

pyautogui.press('Esc')

# Check image to see if inside the safe part of ruins level 2. Unpause if safe
image_path = 'diablo2Images/ruinsLevel22.jpg'
region = (0, 0, screen_width // 2, screen_height)
location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

if location:
    print(f"Ruins level 2 image found at: {location}")
    pyautogui.press('Esc')
else:
    print("Printing out error: Safe Ruins image not found.")

time.sleep(1)

# left click to walk towards wall
pyautogui.click(50, 900)

time.sleep(1.7)

# right click to teleport over wall and towards level 3
pyautogui.rightClick(30,950)
time.sleep(.27)
pyautogui.rightClick(30,950)

# left click to enter ruins level 3 
pyautogui.moveTo(470, 329, duration=0.75)

pyautogui.click()

time.sleep(1)

# right click teleport 3 times to bottom left. Originally 10, 1010 for X and Y but running into barrels getting stuck
pyautogui.rightClick(20,1010)
time.sleep(.27)
pyautogui.rightClick(20,1010)
time.sleep(.27)
pyautogui.rightClick(20,1010)

# 3 times towards right to reach level 4
pyautogui.moveTo(1850, 905, duration=.3)
pyautogui.rightClick(1850, 905)
time.sleep(.27)
pyautogui.rightClick(1850, 905)
time.sleep(.27)
pyautogui.rightClick(1850, 905)

# move mouse above entrance
pyautogui.moveTo(898, 200, duration=0.15)

# try to find entrance image and click on it
try:
    image_path = 'diablo2Images/ruinsLevel4Entrance2.jpg'
    region = (0, 0, screen_width, screen_height)
    location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)
    if location:
        print(f"Ruins level 4 ENTRANCE image found at: {location}")
    pyautogui.moveTo(location.left + 75, location.top + 75, duration=0.6)
    pyautogui.click()

except Exception as e:
    print(f"Error. Can't find level 4 Entrance: {e}")

time.sleep(0.5)

pyautogui.press('Esc')

# Check image to see if inside the safe part of ruins level 4. Unpause if at level 4
image_path = 'diablo2Images/ruinsLevel4.jpg'
region = (screen_width // 2, 0, screen_width // 2, screen_height)
location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

if location:
    print(f"Ruins level 4 image found at: {location}")
    pyautogui.press('Esc')
else:
    print("Printing out error: Safe Ruins image not found.")

time.sleep(.5)

# teleport towards left to get closer to level 5 entrance
pyautogui.rightClick(0, 215)
time.sleep(.27)
pyautogui.rightClick(0, 215)
time.sleep(.27)
pyautogui.rightClick(0, 215)
time.sleep(.27)

# teleport bottom left to reach level 5 entrance
pyautogui.rightClick(90, 860)
time.sleep(.27)
pyautogui.rightClick(90, 860)
time.sleep(.27)
pyautogui.rightClick(90, 860)
time.sleep(.27)
pyautogui.rightClick(90, 860)

time.sleep(1)

# try to find image of level 5 entrance then click to enter 
try:
    image_path = 'diablo2Images/ruinsLevel5Entrance2.jpg'
    region = (0, 0, screen_width, screen_height)
    location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)
    if location:
        print(f"Ruins level 5 ENTRANCE image found at: {location}")
    pyautogui.moveTo(location.left + 125, location.top + 150, duration=0.6)
    pyautogui.click()

except Exception as e:
    print(f"Error. Can't find level 5 Entrance: {e}")

time.sleep(.5)

pyautogui.press('Esc')

time.sleep(.5)

# check that I am inside level 5 then unpause game
image_path = 'diablo2Images/ruinsLevel53.jpg'
region = (screen_width // 2, 0, screen_width // 2, screen_height)
location = pyautogui.locateOnScreen(image_path, confidence=0.6, region=region)

if location:
    print(f"Ruins level 5 image found at: {location}")
    pyautogui.press('Esc')
else:
    print("Printing out error: Ruins level 5 image not found.")

# teleport to countess
time.sleep(.27)
pyautogui.rightClick(1815, 148)
time.sleep(.27)
pyautogui.rightClick(1815, 148)
time.sleep(.27)
pyautogui.rightClick(1815, 148)
time.sleep(.27)

# pyautogui.press('Esc')

# cast Poison Nova
pyautogui.press('F4')
time.sleep(.1)
pyautogui.rightClick()

# cast Decrepify
time.sleep(.1)
pyautogui.press('F8')
time.sleep(.3)
pyautogui.rightClick(1262, 413)
time.sleep(.3)
pyautogui.rightClick(964, 338)
time.sleep(.3)
pyautogui.rightClick(793, 443)
time.sleep(.3)

# cast Poison Nova
pyautogui.press('F4')
time.sleep(.1)
pyautogui.rightClick()

# cast Decrepify
time.sleep(.1)
pyautogui.press('F8')
time.sleep(.3)
pyautogui.rightClick(1262, 413)
time.sleep(.3)
pyautogui.rightClick(964, 338)
time.sleep(.3)
pyautogui.rightClick(793, 443)
time.sleep(.3)

# cast Poison Nova
pyautogui.press('F4')
time.sleep(.1)
pyautogui.rightClick()

# press Alt to view loot
time.sleep(.1)
pyautogui.press('alt')

# cast Corpse Explosion 
time.sleep(.1)
pyautogui.press('F2')
time.sleep(.3)
pyautogui.rightClick(964, 338)
time.sleep(.3)
pyautogui.rightClick(964, 338)
time.sleep(.3)
pyautogui.rightClick(964, 338)

time.sleep(.1)

# look for loot
lootImages = ['ring.jpg', 'amulet.jpg', 'umRune.jpg', 'pulRune.jpg', 'malRune.jpg', 'lemRune.jpg', 'istRune.jpg']

for image in lootImages:
    try:
        image_path = f"diablo2Images/loot/{image}"
        region = (0, 0, screen_width, screen_height)
        location = pyautogui.locateOnScreen(image_path, confidence=0.9, region=region)
        if location:
            print(f"{image} found!!!")
        pyautogui.moveTo(location.left + 10, location.top + 10, duration=0.5)
        pyautogui.click()

    except Exception as e:
        print(f"")

# pyautogui.click()
time.sleep(.5)

for image in lootImages:
    try:
        image_path = f"diablo2Images/loot/{image}"
        region = (0, 0, screen_width, screen_height)
        location = pyautogui.locateOnScreen(image_path, confidence=0.9, region=region)
        if location:
            print(f"{image} found!!!")
        pyautogui.moveTo(location.left + 20, location.top + 15, duration=0.4)
        pyautogui.click()

    except Exception as e:
        print(f"")

time.sleep(1)

pyautogui.press('esc')

# select save and quit
time.sleep(.2)
pyautogui.click(936, 474)

# wait for menu to appear
time.sleep(7)

# start over and select Poison character
repeatCountessRun.repeatCountess()

# select save and quit
time.sleep(.2)
pyautogui.click(936, 474)

# wait for menu to appear
time.sleep(7)

# start over and select Poison character
repeatCountessRun.repeatCountess()