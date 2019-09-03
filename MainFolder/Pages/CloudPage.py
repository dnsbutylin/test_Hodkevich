from MainFolder.Locators import Locator
from selenium.webdriver.common.by import By
from MainFolder.Tools.Loger import *


class CloudPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.upload_button = self.driver.find_element(By.XPATH, Locator.upload_button)

    def click_upload_button(self):
        main.info('Click upload button')
        self.upload_button.click()

    def upload_picture(self, path_to_picture):
        main.info('Upload picture')
        self.driver.find_element(By.XPATH, Locator.input_picture_button).send_keys(path_to_picture)

    def check_replace_button_exist(self):
        if self.driver.find_elements(By.XPATH, Locator.replace_button):
            main.info('Replace button exist')
            return True
        else:
            main.info('Replace button does not exist')
            return False

    def click_replace_button(self):
        main.info('Replace picture')
        self.driver.find_element(By.XPATH, Locator.replace_button).click()

    def click_save_both_button(self):
        main.info('Save both pictures')
        self.driver.find_element(By.XPATH, Locator.save_both_button)










