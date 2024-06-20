import pyautogui
import time

screen_width, screen_height = pyautogui.size()

def findImage(imageName, bool):
    image_path = f'diablo2Images/{imageName}.jpg'
    region = (0, 0, screen_width, screen_height)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"{imageName} found.")
            if bool:
                pyautogui.click(x=location.left, y=location.top)
    
    except Exception as e: 
        print(f"Printing out error: {imageName} image not found.")
        print(f"An error occurred: {e}")

def findD2Icon():
    image_path = f'diablo2Images/diablo2icon.jpg'
    region = (0, screen_height * 7 // 8, screen_width, screen_height // 8)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"diablo2icon found.")
            pyautogui.click(x=location.left, y=location.top)
    
    except Exception as e: 
        print(f"Printing out error: diablo2icon image not found.")
        print(f"An error occurred: {e}")

def findPoisonName():
    image_path = f'diablo2Images/poisonName.jpg'
    region = (screen_width // 2, 0, screen_width // 2, screen_height)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"Poison name found.")
            pyautogui.doubleClick(x=location.left, y=location.top)
    
    except Exception as e: 
        print(f"Printing out error: poisonName image not found.")
        print(f"An error occurred: {e}")

def findHellDifficulty():
    image_path = 'diablo2Images/hellDifficulty.jpg'
    region = (screen_width * 2 // 5, screen_height * 2 // 5, screen_width // 5, screen_height // 5)
    location = pyautogui.locateOnScreen(image_path, confidence=0.8, region=region)

    if location:
        print(f"Hell difficulty found at: {location}")
        pyautogui.click(x=location.left, y=location.top)
    else:
        print("Printing out error: Hell difficulty image not found.")

def checkGameStarted():
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

def ruinsEntrance():
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

def clickWaypoint(): 
    pyautogui.moveTo(856, 0, duration=.1)
    pyautogui.moveTo(856, 103, duration=.5)
    pyautogui.click()

    time.sleep(1)

    # click Black Marsh waypoint
    pyautogui.click(x=366, y=515)

def reachRuins2():
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

    # try searching for image of entrance to level 2
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