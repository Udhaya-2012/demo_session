import pyautogui
import time
import pyperclip
import webbrowser

# Step 1: Open browser (Default)
webbrowser.open("https://www.google.com")
time.sleep(5)  # Wait for browser to open

# Step 2: Type "cricket score" in Google search bar
search_query = "cricket score"
pyperclip.copy(search_query)  # Use clipboard to paste
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)  # Wait for results to load

# Step 3: Click the first link (approx position, adjust as needed)
pyautogui.moveTo(400, 300)  # Approx position of the first result
pyautogui.click()
