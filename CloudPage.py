
from Locators import Locator
from selenium.webdriver.common.by import By



class CloudPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.upload_button = driver.findelement(By.CSS_SELECTOR, Locator.upload_button)
        self.input_picture_button = driver.findelement(By.XPATH, Locator.input_picture_button)
        self.replace_button = driver.findelement(By.XPATH, Locator.replace_button)
        self.save_both_button = driver.findelement(By.XPATH, Locator.save_both_button)

    def click_upload_button(self):
        self.upload_button.click()

    def pass_in_input_picture_button(self, path_to_picture):
        self.input_picture_button.send_keys(path_to_picture)

    def click_replace_button(self):
        self.replace_button.click()

    def save_both_button(self):
        self.save_both_button.click()





