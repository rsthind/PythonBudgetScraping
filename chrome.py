import time
from selenium import webdriver
import os

DRIVER_PATH = os.getcwd() + "/chromedriver"
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.get("http://en.wikipedia.org")
print(driver.title)
time.sleep(8)
driver.quit()
