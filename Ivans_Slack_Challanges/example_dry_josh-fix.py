from http import cookies
from selenium import webdriver
from selenium.webdriver.common.by import By

#%%
class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    
    def click(self,xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()