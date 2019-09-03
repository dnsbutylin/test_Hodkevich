from MainFolder.Core.Loger import *
from MainFolder.Core.Locators import Locator
from selenium.webdriver.common.by import By


class AutorizationMailRuPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_submit_button(self):
        main.info('Confirm entry')
        self.driver.find_element(By.CSS_SELECTOR, Locator.submit_button).click()

    def get_mail_error_massege(self):
        '''Присваиваем аттрибуту self.mail_error_massege елементт и возвращаем поле Text в функцию'''
        self.mail_error_massege = self.driver.find_element(By.ID, Locator.mail_error_massege)
        return self.mail_error_massege.text

    def set_username(self, username):
        main.info('Enter username')
        self.driver.find_element(By.ID, Locator.username).send_keys(username)

    def set_password(self, password):
        main.info('Enter password')
        self.driver.find_element(By.ID, Locator.password).send_keys(password)

    def get_username_element(self):
        '''Присваиваем аттрибуту self.username елементт и возвращаем это же значение переменной в функцию'''
        self.username = self.driver.find_element(By.ID, Locator.username)
        return self.driver.find_element(By.ID, Locator.username)

    def get_password_element(self):
        '''Присваиваем аттрибуту self.password елементт и возвращаем это же значение переменной в функцию'''
        self.password = self.driver.find_element(By.ID, Locator.password)
        return self.driver.find_element(By.ID, Locator.password)


