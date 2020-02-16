from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time
import os

class AmazonScrape(object):

    def __init__(self, items):
        self.amazon_url = "https://www.amazon.com/"
        self.items = items

        #self.profile = webdriver.ChromeProfile()
        #self.options = Options()
        DRIVER_PATH = os.getcwd() + "/chromedriver"
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        self.driver.get(self.amazon_url)

    def search_items(self):
        urls = []
        prices = []
        names = []
        for item in self.items:
            print(f"Searching for {item}.")

            self.driver.get(self.amazon_url)

            search_input = self.driver.find_element_by_id("twotabsearchtextbox")
            search_input.send_keys(item)

            time.sleep(2)

            search_button = self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
            search_button.click()

            time.sleep(2)

items = ["toothpaste"]
amazon_scrape = AmazonScrape(items)
amazon_scrape.search_items()
