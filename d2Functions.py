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