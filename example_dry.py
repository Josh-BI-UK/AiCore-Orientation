from http import cookies
from selenium import webdriver
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def click_button(self, xpath):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def click_accept_cookies(self, xpath):
        cookies_button = self.driver.find_element(By.XPATH, xpath)
        cookies_button.click()

    def click_search_button(self, xpath):
        search_button = self.driver.find_element(By.XPATH, xpath)
        search_button.click()

    def click_add_to_cart(self, xpath):
        add_to_cart_button = self.driver.find_element(By.XPATH, xpath)
        add_to_cart_button.click()