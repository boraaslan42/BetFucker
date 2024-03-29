from seleniumbase import Driver
import time
driver = Driver(uc=True)

# Set up the WebDriver (assuming Chrome)
url = "https://meridianbet.me/en/betting"

# Load the webpage
driver.get(url)
time.sleep(4)

# Get the page source
page_source = driver.page_source

# Save the page source to a file
with open("meridianbet", "w", encoding="utf-8") as file:
    file.write(page_source)

# Close the WebDriver
driver.quit()

