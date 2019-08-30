# -*- coding: utf-8 -*-
from selenium import webdriver
import hashlib
import unittest, time
import os, os.path

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


PATH_TO_PICTURE = "C:\\Vg3bhs0RG1g.jpg"
PICTURE_NAME = 'Vg3bhs0RG1g.jpg'
USERNAME = 'testaccount.2000'
PASSWORD = 'qwe321!qwe'
TIME_TO_WAIT = 2

class UntitledTestCase(unittest.TestCase):

    def setUp(self):

        chrome_options = webdriver.ChromeOptions() # Меняем опции у браузера для скачивания файла в нужную директорию
        prefs = {'download.default_directory': 'C:\\Download_from_mailru\\'} # Путь к директории для скачивания файла
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(TIME_TO_WAIT)

    def test_untitled_test_case(self):

        driver = self.driver
        self.open_mail_ru(driver)
        self.login(driver, USERNAME, PASSWORD)
        self.open_cloud_page(driver)
        self.switch_window(driver)
        self.upload_picture(driver, PATH_TO_PICTURE)
        self.download_picture(driver, PICTURE_NAME)
        self.remove_picture(driver, PICTURE_NAME)

    def remove_picture(self, driver, picture_name):
        self.open_picture_page(driver, picture_name)
        self.close_advertising(driver)
        # Нажимаем удалить
        driver.find_element_by_css_selector(
            "div.b-toolbar__btn.b-toolbar__btn_invert.b-toolbar__btn_data-remove.b-toolbar__btn_grouped.b-toolbar__btn"
            "_grouped_first.b-toolbar__btn_grouped_last > span.b-toolbar__btn__text.b-toolbar__btn__text_pad").click()
        driver.find_element_by_xpath("//div[3]/div/button/span").click() # Подтверждаем удаление
        time.sleep(TIME_TO_WAIT)

    def download_picture(self, driver, picture_name):
        self.open_picture_page(driver, picture_name)
        self.close_advertising(driver)
        driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/span").click()  # Нажимаем скачать
        time.sleep(TIME_TO_WAIT * 2)  # Ждем загрузку

    def open_picture_page(self, driver, picture_name):
        driver.get('https://cloud.mail.ru/home/%s' % picture_name)  # Переходим на страницу с картинкой

    def close_advertising(self, driver):
        if driver.find_elements_by_css_selector("svg.Dialog__close--1rKyk > path"):  # Если есть реклама
            driver.find_element_by_css_selector("svg.Dialog__close--1rKyk > path").click()  # Нажимаем закрыть
        if driver.find_elements_by_css_selector("div.b-panel__close__icon"):  # Если есть реклама
            driver.find_element_by_css_selector("div.b-panel__close__icon").click()  # НАжимаем закрыть
        time.sleep(TIME_TO_WAIT)

    def upload_picture(self, driver, path_to_picture):
        driver.find_element_by_css_selector(
            "span.b-toolbar__btn__text.b-toolbar__btn__text_pad").click()  # Нажимаем кнопку загрузить
        # Добавляем картинку (пришлось использовать xpath)
        driver.find_element_by_xpath("//div[2]/div/input").send_keys(path_to_picture)
        time.sleep(TIME_TO_WAIT)

    def switch_window(self, driver):
        driver.switch_to_window(driver.window_handles[1]) # Переходим во 2ю вкладку

    def open_cloud_page(self, driver):
        # Кликаем по ссылке, со страницы mail.ru, переходим в облако
        driver.find_element_by_css_selector("span.widget__ico.widget__ico_cloud").click()

    def login(self, driver, username, password):
        driver.find_element_by_id("mailbox:login").send_keys(username) # Имя пользователя
        driver.find_element_by_id("mailbox:password").send_keys(password) # Пароль
        driver.find_element_by_css_selector("input.o-control").click() # Подтверждаем ввод
        time.sleep(TIME_TO_WAIT)

    def open_mail_ru(self, driver):
        driver.get("https://mail.ru/")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
