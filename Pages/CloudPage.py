from Core.Locators import Locator
from selenium.webdriver.common.by import By
from Core.Loger import *


class CloudPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_upload_button(self):
        log.info('Click upload button')
        self.driver.find_element(By.XPATH, Locator.upload_button).click()

    def upload_picture(self, path_to_picture):
        log.info('Upload picture')
        self.driver.find_element(By.XPATH, Locator.input_picture_button).send_keys(path_to_picture)

    def check_replace_button_exist(self):
        if self.driver.find_elements(By.XPATH, Locator.replace_button):
            log.info('Replace button exist')
        else:
            log.info('Replace button does not exist')

    def click_replace_button(self):
        log.info('Replace picture')
        self.driver.find_element(By.XPATH, Locator.replace_button).click()

    def wait_upload(self, second):
        import time
        i = 0
        while i <= second:
            while self.driver.find_element(By.CSS_SELECTOR, Locator.check_upload_locator).text != "Загрузка завершена":
                time.sleep(1)
                i += 1
            else:
                i += 1










