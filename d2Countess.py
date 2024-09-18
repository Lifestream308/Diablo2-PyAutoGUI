import pyautogui
import time
import sys
import d2Functions
import keyboard

# Shift + Window button + S key will allow me to make screenshot of certain area I choose

# Each run takes about 1 minute, 30 seconds to complete. 40 perfect runs /hr. 35 safer number. 70/2. 105/3. 140/4. 175/5. 210/6. 280/8. 350/10.

loopsCompleted = 0
totalLoops = 100
running = True
lootDropped = {}

screen_width, screen_height = pyautogui.size()

def stopScript():
    global running
    print("You pressed 'q'. Exiting...")
    running = False

keyboard.add_hotkey('q', stopScript)
keyboard.add_hotkey('tab', stopScript)

def startCountess():
    global loopsCompleted
    global totalLoops
    global running
    global lootDropped

    # find d2 icon on bottom screen, click on icon
    d2Functions.findD2Icon()

    time.sleep(1)

    # find Poison pic to select character on right screen, double click, wait 
    d2Functions.findPoisonName()

    time.sleep(1)

    # find Hell pic, click, wait for load
    d2Functions.findHellDifficulty()

    # Should now be in act 1
    time.sleep(11)

    # check if mercenary alive and if game started
    image_path = 'diablo2Images/mercenary.jpg'
    region = (0, 0, screen_width // 5, screen_height // 5)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"Mercenary image found.")
    
    except Exception as e: 
        print(f"Mercenary image not found.")
        # click down + right to move closer to Kashya which is x=900, y=955
        pyautogui.click(x=700, y=955)
        time.sleep(0.5)
        # search multiple times for kashya images
        for i in range(15):
            for j in range(7):
                try:
                    image_path = f"diablo2Images/loot/kashya/kashya{j+1}.jpg"
                    region = (0, 0, screen_width, screen_height)
                    location = pyautogui.locateOnScreen(image_path, confidence=0.65, region=region)
                    # click Kashya if found
                    if location:
                        print(f"kashya{j+1} found!!!")
                        pyautogui.moveTo(location.left + 20, location.top + 15, duration=0.2)
                        pyautogui.click()
                        time.sleep(1)
                        # search for resurrectVik picture option
                        try:
                            image_path = f"diablo2Images/loot/kashya/resurrectVik.jpg"
                            region = (0, 0, screen_width, screen_height)
                            location = pyautogui.locateOnScreen(image_path, confidence=0.9, region=region)
                            # click option to resurrect mercenary if found
                            if location:
                                print(f"Resurrect Vik picture found!!!")
                                pyautogui.moveTo(location.left + 20, location.top + 15, duration=0.2)
                                pyautogui.click()
                                time.sleep(0.3)
                                if "Resurrections" not in lootDropped:
                                    lootDropped["Resurrections"] = 1
                                else:
                                    lootDropped["Resurrections"] += 1
                                # press escape button 2 times to exit dialogue and bring up save and exit menu
                                pyautogui.press('esc')
                                time.sleep(1)
                                pyautogui.press('esc')
                                time.sleep(1)
                                # press save and exit button
                                pyautogui.click(936, 474)
                                # wait for menu to appear
                                print(f"Previous line of code should have exited to main menu")
                                time.sleep(7)
                                # begin countess runs again and remove sys exit below and above. replace below exit with startCountess?
                                print(f"Next line should startCountess function again")
                                startCountess()
                            else: 
                                print("Resurrect Vik picture not found")
                                
                        except Exception as e:
                            pass

                except Exception as e:
                    pass
        print("Couldn't find Kashya image. Running into issue here where sometimes run once more, then stops at main menu? commented out sys exit so now will it check if arm pic is found and exit there?")
        # sys.exit()

    # wait and check if loading screen finished, then click halfway to waypoint
    d2Functions.checkGameStarted()

    time.sleep(0.8)

    # click on waypoint
    d2Functions.clickWaypoint()

    # wait for loading screen
    time.sleep(2)

    # select teleport spell, move to ruins entrance and enter
    d2Functions.ruinsEntrance()

    time.sleep(.2)

    # Check image to see if inside the safe part of the ruins. Unpause if safe
    image_path = 'diablo2Images/safeRuins2.jpg'
    region = (0, 0, screen_width // 2, screen_height)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"Safe Ruins found.")
            pyautogui.press('esc')
    
    except Exception as e: 
        print(f"Printing out error: Safe Ruins image not found.")
        print(f"An error occurred: {e}")
        # select save and quit
        time.sleep(1)
        pyautogui.click(936, 474)

        # wait for menu to appear
        time.sleep(7)

        # loop here determines how many times to run counand notess
        while loopsCompleted < totalLoops and running:
            startCountess()
            loopsCompleted += 1
        sys.exit()

    # location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

    # if location:
    #     print(f"Safe. Ruins image found at: {location}")
    #     pyautogui.press('Esc')
    # else:
    #     print("Printing out error: Safe Ruins image not found.")

    time.sleep(.5)

    # click on entrance to ruins officially
    pyautogui.moveTo(545, 543, duration=.5)
    pyautogui.click()
    time.sleep(.75)

    # right click teleport to right side of screen closer to level 2
    d2Functions.reachRuins2()

    time.sleep(0.8)

    pyautogui.press('Esc')

    # Check image to see if inside the safe part of ruins level 2. Unpause if safe
    image_path = 'diablo2Images/ruinsLevel22.jpg'
    region = (0, 0, screen_width // 2, screen_height)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"Ruins Level 2 found.")
            pyautogui.press('esc')
    
    except Exception as e: 
        print(f"Printing out error: Ruins Level 2 image not found.")
        print(f"An error occurred: {e}")
        # select save and quit
        time.sleep(1)
        pyautogui.click(936, 474)

        # wait for menu to appear
        time.sleep(7)

        # loop here determines how many times to run counand notess
        while loopsCompleted < totalLoops and running:
            startCountess()
            loopsCompleted += 1
        sys.exit()

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

    time.sleep(.1)

    # Check image to see if inside the safe part of ruins level 4. Unpause if at level 4
    image_path = 'diablo2Images/ruinsLevel4.jpg'
    region = (screen_width // 2, 0, screen_width // 2, screen_height)

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7, region=region)

        if location:
            print(f"Ruins Level 4 found.")
            pyautogui.press('esc')
    
    except Exception as e: 
        print(f"Printing out error: Ruins Level 4 image not found.")
        print(f"An error occurred: {e}")
        # select save and quit
        time.sleep(1)
        pyautogui.click(936, 474)

        # wait for menu to appear
        time.sleep(7)

        # loop here determines how many times to run counand notess
        while loopsCompleted < totalLoops and running:
            startCountess()
            loopsCompleted += 1
        sys.exit()

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

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.6, region=region)

        if location:
            print(f"Ruins Level 5 found.")
            pyautogui.press('esc')
    
    except Exception as e: 
        print(f"Printing out error: Ruins Level 5 image not found.")
        print(f"An error occurred: {e}")
        # select save and quit
        time.sleep(1)
        pyautogui.click(936, 474)

        # wait for menu to appear
        time.sleep(7)

        # loop here determines how many times to run counand notess
        while loopsCompleted < totalLoops and running:
            startCountess()
            loopsCompleted += 1
        sys.exit()

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
    pyautogui.rightClick(964, 338)
    time.sleep(.3)
    pyautogui.rightClick(1200, 440)
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
    pyautogui.rightClick(964, 338)
    time.sleep(.3)
    pyautogui.rightClick(1200, 440)
    time.sleep(.3)
    pyautogui.rightClick(793, 443)
    time.sleep(.3)

    # press Alt to view loot
    pyautogui.press('alt')
    time.sleep(.1)

    # cast Poison Nova
    pyautogui.press('F4')
    time.sleep(.1)
    pyautogui.rightClick()

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
    lootImages = [
                'ring', 
                'amulet', 
                'vexRune', 
                'gulRune', 
                'istRune', 
                'malRune', 
                'umRune', 
                'pulRune', 
                'charm', 
                'jewel', 
                # 'lemRune', 
                # 'diamond', 
                # 'emerald', 
                'ruby', 
                'sapphire', 
                'amethyst', 
                # 'topaz', 
                # 'flawedDiamond', 
                # 'skull', 
                'gold']

    for i in range (2):
        for image in lootImages:
            try:
                image_path = f"diablo2Images/loot/{image}.jpg"
                region = (0, 0, screen_width, screen_height)
                location = pyautogui.locateOnScreen(image_path, confidence=0.9, region=region)
                if location:
                    print(f"{image} found!!!")
                    pyautogui.moveTo(location.left + 20, location.top + 15, duration=0.3)
                    pyautogui.click()
                    # add the dropped loot to dictionary
                    if image not in lootDropped:
                        lootDropped[image] = 1
                    else:
                        lootDropped[image] += 1
                    time.sleep(.2)

            except Exception as e:
                pass
                # print(f"")
        if i >= 1:
            print(lootDropped)

        # pyautogui.click()
        time.sleep(.5)

    time.sleep(.5)

    pyautogui.press('esc')

    # select save and quit and then will wait for main menu character selection screen
    time.sleep(1)
    pyautogui.click(936, 474)

    # wait for menu to appear
    time.sleep(7)

    print(f"{loopsCompleted+1} Completed")

# loop here determines how many times to run countess
while loopsCompleted < totalLoops and running:
    startCountess()
    loopsCompleted += 1