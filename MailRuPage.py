
from Locators import Locator
from selenium.webdriver.common.by import By



class MailRuPage(object):

    def __init__(self, driver):
        self.on_cloud_page_button = driver.find_element(By.CSS_SELECTOR, Locator.on_cloud_page_button)

    def click_on_cloud_page_button(self):
        self.on_cloud_page_button.click()

