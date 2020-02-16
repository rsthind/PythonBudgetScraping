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

class AmazonDeals(object):

    def __init__(self):
        self.amazon_url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb_azl"

        DRIVER_PATH = os.getcwd() + "/chromedriver"
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        self.driver.get(self.amazon_url)

    def search_items(self):
        urls = []
        prices = []
        names = []
        for x in range(0, 8):
            print(f"Searching for {x} of 8 deals.")

            self.driver.get(self.amazon_url)

            first_result = self.driver.find_element_by_id("101_dealView_" + str(x))
            image = first_result.find_element_by_id('dealImage')
            url = image.get_attribute("href")

            print(url)
            price = self.get_product_price(url)
            name = self.get_product_name(url)

            prices.append(price)
            urls.append(url)
            names.append(name)

            print(name)
            print(price)
            print(url)

            time.sleep(2)

        return prices, urls, names


    def get_product_price(self, url):
        self.driver.get(url)
        price = None
        try:
            price = self.driver.find_element_by_id("priceblock_ourprice").text
        except:
            pass

        try:
            price = self.driver.find_element_by_id("priceblock_dealprice").text
        except:
            pass


        if price is None:
            price = "Not available"

        else:
            non_decimal = re.compile(r'[^\d.]+')
            price = non_decimal.sub('', price)

        return price


    def get_product_name(self, url):
        self.driver.get(url)
        product_name = None
        try:
            product_name = self.driver.find_element_by_id("productTitle").text
        except:
            pass

        if product_name is None:
            product_name = "Not available"

        return product_name

#items = ["toothpaste"]
#amazon_scrape = AmazonScrape(items)
#amazon_scrape.search_items()
