from MainFolder.Pages.AutorizationMailRuPage import AutorizationMailRuPage
from MainFolder.Pages.MailRuPage import MailRuPage
from MainFolder.Pages.CloudPage import CloudPage
from MainFolder.Pages.PicturePage import PicturePage
from selenium import webdriver
from MainFolder.Core.Tools import *
from MainFolder.Core.Loger import *
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()  # Меняем опции у браузера для скачивания файла в нужную директорию
        prefs = {'download.default_directory': 'C:\\Download_from_mailru\\'}  # Путь к директории для скачивания файла
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(6)

    def test_upload_download_remove_picture(self):
        driver = self.driver
        driver.set_page_load_timeout(20)
        try:
            log.info('Go to https://mail.ru/')
            driver.get('https://mail.ru/')
        except:
            log.error("driver.get('https://mail.ru/') failed")
        try:
            authorization = AutorizationMailRuPage(driver) # Создаем экземпляр класса страницы авторизации
            authorization.set_username(USERNAME) # Вводим логин
            authorization.set_password(PASSWORD) # Вводим пароль
            authorization.click_submit_button() # Подтверждаем ввод
        except:
            log.error('Autorization failed')

        mailru = MailRuPage(driver) # Создаем экземпляр класса страницы mail.ru
        # Ждем пока не появиться кнопка "Перейти в облако"
        mailru.wait_animation()
        try:
            log.info('Go to https://cloud.mail.ru/home')
            self.driver.get('https://cloud.mail.ru/home') # Переходим на страницу облака
        except:
            log.error('did not go to the https://cloud.mail.ru/home page')
        old_hesh = (md5(PATH_TO_PICTURE)) # Получаем хеш картинки до загрузки
        cloud = CloudPage(driver) # Создаем экземпляр класса страницы облака
        try:
            cloud.click_upload_button() # Кликаем по кнопке загрузкить
            cloud.upload_picture(PATH_TO_PICTURE) # Загружаем картинку
            if cloud.check_replace_button_exist(): # Если паявилась кнопка заменить?
                cloud.click_replace_button() # Кликаем заменить
        except:
            log.error('not uploaded picture')
        # Каждую секунду проверяем завершилась ли загрузка (Максимум 5 сек)
        cloud.wait_upload(5)
        try:
            log.info('Open picture page')
            driver.get('https://cloud.mail.ru/home/%s' % PICTURE_NAME)  # Переходим на страницу с картинкой
        except:
            log.info('Cant go to page https://cloud.mail.ru/home/%s' % PICTURE_NAME)

        picture = PicturePage(driver) # Создаем экземпляр класса страницы картинки
        try:
            picture.close_advertising() # Закрываем рекламу
        except:
            log.error('Advertising did not close')
        # Создаем папку C:\Download_from_mailru, если её нет
        if 'Download_from_mailru' not in os.listdir('C:\\'):
            try:
                os.mkdir('Download_from_mailru')
                log.info('Create folder for download')
            except:
                log.error('Cannot create folder')
        else:
            log.info('Folder for download exist')
        picture.click_download_button() # Нажимаем кнопку загрузить
        # Каждую секунду проверяем не появилась ли картинка в загрузках
        picture.wait_download(5)
        new_hesh = (md5('C:\\Download_from_mailru\\' + PICTURE_NAME))  # Берем хеш картинки после загрузки
        assert old_hesh == new_hesh  # Сравниваем хеш до и после загруки
        picture.click_delete_button() # Нажимаем удалить
        picture.click_confirm_delete_button() # Подтверждаем удаление
        remove_folder_contents('C:\\Download_from_mailru')  # Чистим содержимое папки

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()









