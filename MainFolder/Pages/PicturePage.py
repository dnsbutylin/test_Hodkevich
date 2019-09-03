from MainFolder.Core.Locators import Locator
from selenium.webdriver.common.by import By
from MainFolder.Core.Loger import *
from MainFolder.Core.Tools import *


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
        log.info('Close "svg.Dialog__close--1rKyk > path" adversing')
        self.driver.find_element(By.CSS_SELECTOR, Locator.close_advertising1).click()

    def close_advertising2(self):
        log.info('Close "div.b-panel__close__icon" adversing')
        self.driver.find_element(By.CSS_SELECTOR, Locator.close_advertising2).click()

    def click_delete_button(self):
        log.info('Click delete button')
        self.driver.find_element(By.XPATH, Locator.delete_button).click()

    def click_confirm_delete_button(self):
        log.info('Click confirm delete button')
        self.driver.find_element(By.XPATH, Locator.confirm_delete_button).click()

    def click_download_button(self):
        log.info('Click download button')
        self.driver.find_element(By.XPATH, Locator.download_button).click()

    def close_advertising(self):
        if self.check_advertising1():
            self.close_advertising1()
        if self.check_advertising2():
            self.close_advertising2()

    def wait_download(self, second):
        import time
        i = 0
        while i <= second:
            while PICTURE_NAME not in os.listdir('C:\\Download_from_mailru'):  # Ожидаем пока не появится
                time.sleep(1)
                i += 1
            else:
                i += 1




