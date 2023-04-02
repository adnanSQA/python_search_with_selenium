
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Website url
URL = "https://www.python.org/"
# Chromium Drivers
# Replace path of the chromium drivers with the directory in which you have your chromium drivers 
PATH = Service('C:\Program Files (x86)\chromedriver.exe')
# i am using google chrome that's why i have webdriver.chrome option 
# You can replace it with , edge options, firefox options etc.
OP = webdriver.ChromeOptions()
DRIVER = webdriver.Chrome(service=PATH, options=OP)

#  the search keyword 
search_keyword = "cricket"
# Navigate to the website using get method 
DRIVER.get(URL) 

# Find the Search field
search_field = DRIVER.find_element(By.NAME, 'q')

# Type anything on the website 
search_field.send_keys(search_keyword)


# Search button 
search_button = DRIVER.find_element(By.ID, 'submit')
search_button.click()
time.sleep(4) 

