from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create Chrome WebDriver
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")
time.sleep(2)

# Find Google search box using NAME
search_box = driver.find_element(By.NAME, "q")

# Search using send_keys()
search_box.send_keys("Python programming")
search_box.submit()

time.sleep(3)

# Refresh page
driver.refresh()
time.sleep(2)

# Find multiple links
links = driver.find_elements(By.TAG_NAME, "a")

# Display links
print("Total links:", len(links))

for link in links[:10]:
    print(link.text)

# Open Amazon
driver.get("https://www.amazon.in")
time.sleep(3)

# Find element using CLASS_NAME
try:
    search = driver.find_element(By.CLASS_NAME, "nav-search-field")
    print("Class element found")
except:
    print("Class element not found")

# Find element using LINK_TEXT
try:
    link = driver.find_element(By.LINK_TEXT, "Today's Deals")
    print("Link found:", link.text)
except:
    print("Link not found")

# Find element using XPATH
try:
    logo = driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
    print("Amazon logo found")
except:
    print("Logo not found")

# Close browser
driver.quit()