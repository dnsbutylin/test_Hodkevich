import unittest
from EnvironmentSetUp import EnvironmentSetUp
from AutorizationMailRuPage import AutorizationMailRuPage
from MailRuPage import MailRuPage
from CloudPage import CloudPage
from PicturePage import PicturePage
from Locators import Locator
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib


class TestCase(EnvironmentSetUp):

    def test_upload_download_remove_picture(self):

        driver = self.driver
        try:
            driver.get('https://mail.ru/')
        except:
            pass
        driver.set_page_load_timeout(20)

        authorization = AutorizationMailRuPage(driver)
        authorization.set_username('testaccount.2000')
        authorization.set_password('qwe321!qwe')
        authorization.click_submit_button()

        mailru = MailRuPage(driver)
        # Ждем пока не появиться кнопка "Перейти в облако"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_selection_state_to_be(mailru.on_cloud_page_button, False))
        try:
            driver.get('https://cloud.mail.ru/home')
        except:
            pass
        

