from MainFolder.Locators import Locator
from selenium.webdriver.common.by import By
from MainFolder.Tools.Loger import *


class PicturePage():

    def __init__(self, driver):
        self.driver = driver

    def check_advertising1(self):
        if self.driver.find_elements(By.CSS_SELECTOR, Locator.close_advertising1):
            return True
        else:
            return False

    def check_advertising2(self):
        if self.driver.find_elements(By.CSS_SELECTOR, Locator.close_advertising2):
            return True
        else:
            return False

    def close_advertising1(self):
        main.info('Close "svg.Dialog__close--1rKyk > path" adversing')
        self.driver.find_element(By.CSS_SELECTOR, Locator.close_advertising1).click()

    def close_advertising2(self):
        main.info('Close "div.b-panel__close__icon" adversing')
        self.driver.find_element(By.CSS_SELECTOR, Locator.close_advertising2).click()

    def click_delete_button(self):
        main.info('Click delete button')
        self.driver.find_element(By.XPATH, Locator.delete_button).click()

    def click_confirm_delete_button(self):
        main.info('Click confirm delete button')
        self.driver.find_element(By.XPATH, Locator.confirm_delete_button).click()

    def click_download_button(self):
        main.info('Click download button')
        self.driver.find_element(By.XPATH, Locator.download_button).click()

    def close_advertising(self):
        if self.check_advertising1():
            self.close_advertising1()
        if self.check_advertising2():
            self.close_advertising2()




