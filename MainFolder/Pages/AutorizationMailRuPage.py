from MainFolder.Core.Loger import *
from MainFolder.Core.Locators import Locator
from selenium.webdriver.common.by import By


class AutorizationMailRuPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_submit_button(self):
        log.info('Confirm entry')
        self.driver.find_element(By.CSS_SELECTOR, Locator.submit_button).click()

    def set_username(self, username):
        log.info('Enter username')
        self.driver.find_element(By.ID, Locator.username).send_keys(username)

    def set_password(self, password):
        log.info('Enter password')
        self.driver.find_element(By.ID, Locator.password).send_keys(password)


