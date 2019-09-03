from selenium.webdriver.common.by import By
from Page_Object_Pattern.Fixture.EnvironmentSetUp import EnvironmentSetUp
from Page_Object_Pattern.Pages.AutorizationMailRuPage import AutorizationMailRuPage
from Page_Object_Pattern.Pages.MailRuPage import MailRuPage
from Page_Object_Pattern.Pages.CloudPage import CloudPage
from Page_Object_Pattern.Pages.PicturePage import PicturePage
from Page_Object_Pattern.Locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Pattern.Tools.Tools import *
import time
from Page_Object_Pattern.Loger.Loger import *


class TestCase(EnvironmentSetUp):

    def test_upload_download_remove_picture(self):
        driver = self.driver
        driver.set_page_load_timeout(20)
        try:
            main.info('Go to https://mail.ru/')
            driver.get('https://mail.ru/')
        except:
            main.error("driver.get('https://mail.ru/') failed")

        try:
            authorization = AutorizationMailRuPage(driver) # Создаем экземпляр класса страницы авторизации
            authorization.set_username(USERNAME) # Вводим логин
            authorization.set_password(PASSWORD) # Вводим пароль
            authorization.click_submit_button() # Подтверждаем ввод
        except:
            main.error('Autorization failed')

        mailru = MailRuPage(driver) # Создаем экземпляр класса страницы mail.ru
        # Ждем пока не появиться кнопка "Перейти в облако"
        WebDriverWait(driver, 10).until(EC.element_selection_state_to_be(mailru.on_cloud_page_button, False))
        try:
            main.info('Go to https://cloud.mail.ru/home')
            self.driver.get('https://cloud.mail.ru/home') # Переходим на страницу облака
        except:
            main.error('did not go to the https://cloud.mail.ru/home page')

        old_hesh = (md5(PATH_TO_PICTURE)) # Получаем хеш картинки до загрузки
        cloud = CloudPage(driver) # Создаем экземпляр класса страницы облака
        try:
            cloud.click_upload_button() # Кликаем по кнопке загрузкить
            cloud.upload_picture(PATH_TO_PICTURE) # Загружаем картинку
            if cloud.check_replace_button_exist(): # Если паявилась кнопка заменить?
                cloud.click_replace_button() # Кликаем заменить
        except:
            main.error('not uploaded picture')

        # Каждую секунду проверяем завершилась ли загрузка (Максимум 5 сек)
        i = 0
        while i <= 5:
            while self.driver.find_element(By.CSS_SELECTOR, Locator.check_upload_locator).text != "Загрузка завершена":
                time.sleep(1)
                i += 1
            else:
                i += 1
        try:
            main.info('Open picture page')
            driver.get('https://cloud.mail.ru/home/%s' % PICTURE_NAME)  # Переходим на страницу с картинкой
        except:
            main.info('Cant go to page https://cloud.mail.ru/home/%s' % PICTURE_NAME)

        picture = PicturePage(driver) # Создаем экземпляр класса страницы картинки
        try:
            picture.close_advertising() # Закрываем рекламу
        except:
            main.error('Advertising did not close')
        # Создаем папку C:\Download_from_mailru, если её нет
        if 'Download_from_mailru' not in os.listdir('C:\\'):
            try:
                os.mkdir('Download_from_mailru')
                main.info('Create folder for download')
            except:
                main.error('Cannot create folder')
        else:
            main.info('Folder for download exist')

        picture.click_download_button() # Нажимаем кнопку загрузить
        # Каждую секунду проверяем не появилась ли картинка в загрузках
        i = 0
        while i <= 5:
            while PICTURE_NAME not in os.listdir('C:\\Download_from_mailru'):  # Ожидаем пока не появится
                time.sleep(1)
                i += 1
            else:
                i += 1

        new_hesh = (md5('C:\\Download_from_mailru\\' + PICTURE_NAME))  # Берем хеш картинки после загрузки
        assert old_hesh == new_hesh  # Сравниваем хеш до и после загруки
        picture.click_delete_button() # Нажимаем удалить
        picture.click_confirm_delete_button() # Подтверждаем удаление













