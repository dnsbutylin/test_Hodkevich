from selenium import webdriver
import hashlib
import time
import os, os.path, shutil
import logging

PATH_TO_PICTURE = "C:\\Vg3bhs0RG1g.jpg"
PICTURE_NAME = 'Vg3bhs0RG1g.jpg'
USERNAME = 'testaccount.2000'
PASSWORD = 'qwe321!qwe'
TIME_TO_WAIT = 6


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def remove_folder_contents(path):
    shutil.rmtree(path)
    os.makedirs(path)


class Application:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()  # Меняем опции у браузера для скачивания файла в нужную директорию
        prefs = {'download.default_directory': 'C:\\Download_from_mailru\\'}  # Путь к директории для скачивания файла
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(TIME_TO_WAIT)
        # Настройки логера
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        logger_handler = logging.FileHandler('python_logging.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)


    def remove_picture(self, picture_name):
        driver = self.driver
        self.open_picture_page(picture_name)
        self.close_advertising()
        # Нажимаем удалить
        self.logger.info('Click delete')
        driver.find_element_by_css_selector(
            "div.b-toolbar__btn.b-toolbar__btn_invert.b-toolbar__btn_data-remove.b-toolbar__btn_grouped.b-toolbar__btn"
            "_grouped_first.b-toolbar__btn_grouped_last > span.b-toolbar__btn__text.b-toolbar__btn__text_pad").click()
        self.logger.info('Confirm delete')
        driver.find_element_by_xpath("//div[3]/div/button/span").click()  # Подтверждаем удаление
        self.logger.info('Cleaninig folder for download')
        remove_folder_contents('C:\\Download_from_mailru')  # Зачистка содержимого папки
        self.logger.info('Wait %s second' % str(TIME_TO_WAIT) )
        time.sleep(TIME_TO_WAIT)

    def download_picture(self, picture_name):
        driver = self.driver
        self.open_picture_page(picture_name)
        self.close_advertising()
        if 'Download_from_mailru' not in os.listdir('C:\\'):
            os.mkdir('Download_from_mailru')
            self.logger.info('Create folder for download')
        else:
            self.logger.info('Folder for download exist')
        self.logger.info('Click download')
        driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/span").click()  # Нажимаем скачать
        self.logger.info('Wait %s second' % str(TIME_TO_WAIT * 2))
        time.sleep(TIME_TO_WAIT * 2)  # Ждем загрузку

    def open_picture_page(self, picture_name):
        driver = self.driver
        self.logger.info('Open picture page')
        driver.get('https://cloud.mail.ru/home/%s' % picture_name)  # Переходим на страницу с картинкой

    def close_advertising(self):
        driver = self.driver
        self.logger.info('Wait %s second' % str(TIME_TO_WAIT / 2))
        time.sleep(TIME_TO_WAIT / 2)
        if driver.find_elements_by_css_selector("svg.Dialog__close--1rKyk > path"):  # Если есть реклама
            driver.find_element_by_css_selector("svg.Dialog__close--1rKyk > path").click()  # Нажимаем закрыть
            self.logger.info('Close "svg.Dialog__close--1rKyk > path" adversing')
        if driver.find_elements_by_css_selector("div.b-panel__close__icon"):  # Если есть реклама
            driver.find_element_by_css_selector("div.b-panel__close__icon").click()  # НАжимаем закрыть
            self.logger.info('Close "div.b-panel__close__icon" adversing')

    def upload_picture(self, path_to_picture, action='replace'):
        '''Если есть файл с таким же именем, то по умолчанию метод заменяет его на новый
        для сохраниния обоих файлов нужно указать action="save_both"'''
        driver = self.driver
        self.logger.info('Click download button')
        driver.find_element_by_css_selector(
            "span.b-toolbar__btn__text.b-toolbar__btn__text_pad").click()  # Нажимаем кнопку загрузить
        # Добавляем картинку (пришлось использовать xpath)
        self.logger.info('Upload picture')
        driver.find_element_by_xpath("//div[2]/div/input").send_keys(path_to_picture)
        # Если появилось диалоговое окно, выбираем действие в зависимости от указанного параметра
        if driver.find_elements_by_xpath("//div[3]/button/span") and action == 'replace':
            driver.find_element_by_xpath("//div[3]/button/span").click()
            self.logger.info('Replace picture')
        if driver.find_elements_by_xpath("//div[3]/button/span") and action == 'save_both':
            driver.find_element_by_xpath("//div[3]/button[2]/span").click()
            self.logger.info('Save both picture')
        self.logger.info('Wait %s second' % str(TIME_TO_WAIT))
        time.sleep(TIME_TO_WAIT)

    def switch_window(self, i):
        driver = self.driver
        self.logger.info('Switch window')
        driver.switch_to_window(driver.window_handles[i])  # Переходим во 2ю вкладку

    def open_cloud_page(self):
        driver = self.driver
        # Кликаем по ссылке, со страницы mail.ru, переходим в облако
        self.logger.info('Open cloud page')
        driver.find_element_by_css_selector("span.widget__ico.widget__ico_cloud").click()
        self.switch_window(1)

    def login(self, username, password):
        driver = self.driver
        self.logger.info('Enter username')
        driver.find_element_by_id("mailbox:login").send_keys(username)  # Имя пользователя
        self.logger.info('Enter password')
        driver.find_element_by_id("mailbox:password").send_keys(password)  # Пароль
        self.logger.info('Confirm entry')
        driver.find_element_by_css_selector("input.o-control").click()  # Подтверждаем ввод
        time.sleep(TIME_TO_WAIT)

    def open_mail_ru(self):
        driver = self.driver
        self.logger.info('Go to home page')
        driver.get("https://mail.ru/")

    def destroy(self):
        self.driver.quit()
