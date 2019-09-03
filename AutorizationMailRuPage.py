from loger import *
from Locators import Locator
from selenium.webdriver.common.by import By



class AutorizationMailRuPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element(By.ID, Locator.username)
        self.password = driver.find_element(By.ID, Locator.password)
        self.submit_button = driver.find_element(By.CSS_SELECTOR, Locator.submit_button)
        self.mail_error_massege = driver.find_element(By.ID, Locator.mail_error_massege)

    def click_submit_button(self):
        main.info('Confirm entry')
        self.submit_button.click()

    def get_mail_error_massege(self):
        return self.mail_error_massege.text

    def set_username(self, username):
        main.info('Enter username')
        self.username.send_keys(username)


    def set_password(self, password):
        main.info('Enter password')
        self.password.send_keys(password)

