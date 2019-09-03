from MainFolder.Core.Loger import *
from MainFolder.Core.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MailRuPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.on_cloud_page_button = driver.find_element(By.CSS_SELECTOR, Locator.on_cloud_page_button)

    def click_on_cloud_page_button(self):
        main.info('Go to https://cloud.mail.ru/home')
        self.on_cloud_page_button.click()

    def wait_animation(self):
        WebDriverWait(self.driver, 10).until(EC.element_selection_state_to_be(self.on_cloud_page_button, False))



