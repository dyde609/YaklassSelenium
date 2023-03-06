from selenium.webdriver.common.by import By
from yklM import driver
from bs4 import BeautifulSoup

class Subject:
    def __init__(self, name):
        self.name = name
        if driver.current_url != 'https://www.yaklass.ru/p': driver.get('https://www.yaklass.ru/p')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for i in driver.find_elements(By.CLASS_NAME, 'thumb'):
            if i.text == self.name:
                self.link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
                i.click()
                break