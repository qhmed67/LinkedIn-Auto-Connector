import pyautogui
import time
import os
import keyboard


# Configuration
BUTTON_IMAGE = os.path.join(os.path.dirname(__file__), 'connect_button.png')
SCROLL_AMOUNT = -700  # Negative number means scroll down, -700 is optimal for most screens
WAIT_BETWEEN_ACTIONS = 0.5  # Time to wait between clicks (in seconds)
PAGE_LOAD_DELAY = 2  # Time to wait after scrolling for new content to load
MAX_SEARCH_ATTEMPTS = 3  # Number of times to look for buttons before scrolling

# Startup messages
print('Starting LinkedIn Connect Bot...')
print('You have 3 seconds to switch to LinkedIn window (Show all [People you may know based on your recent activity])')
for i in range(3, 0, -1):
    print(f'{i}...')
    time.sleep(1)
print('Bot is now running! Press L to stop')

connections = 0  # Counter for successful connections made

# Main bot loop
while True:
    # Check for stop command
    if keyboard.is_pressed('l'):
        print('L key pressed. Stopping the bot.')
        break
    
    # Search for connect buttons multiple times before deciding to scroll
    buttons_found = False
    for attempt in range(MAX_SEARCH_ATTEMPTS):
        try:
            print(f'Searching for Connect button (attempt {attempt + 1}/{MAX_SEARCH_ATTEMPTS})...')
            location = pyautogui.locateCenterOnScreen(BUTTON_IMAGE, confidence=0.8)
            if location:
                # Found a connect button - click it!
                print(f'Connect button found at {location}, clicking...')
                pyautogui.moveTo(location)
                pyautogui.click()
                connections += 1
                time.sleep(WAIT_BETWEEN_ACTIONS)
                buttons_found = True
            else:
                # No button found this attempt, wait briefly and try again
                print(f'No connect button found on attempt {attempt + 1}')
                time.sleep(WAIT_BETWEEN_ACTIONS)
        except pyautogui.ImageNotFoundException:
            print(f'No connect button found on attempt {attempt + 1}')
            time.sleep(WAIT_BETWEEN_ACTIONS)
    
    # If no buttons found after all attempts, scroll down for new content
    if not buttons_found:
        print(f'No more connect buttons found after {MAX_SEARCH_ATTEMPTS} attempts. Scrolling down ({SCROLL_AMOUNT})...')
        pyautogui.scroll(SCROLL_AMOUNT)
        print('Waiting for new content to load...')
        time.sleep(PAGE_LOAD_DELAY)

# Show final results
print(f'Total connections made: {connections}')


