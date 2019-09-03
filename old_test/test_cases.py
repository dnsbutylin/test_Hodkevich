# -*- coding: utf-8 -*-
import unittest
from old_test.application import *

class Test_case(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_upload_download_remove_picture(self):
        self.app.open_mail_ru() # Заходим на сайт
        self.app.login(username=USERNAME, password=PASSWORD) # Логинимсмя
        self.app.open_cloud_page() # Переходим в облако
        old_hesh = (md5(PATH_TO_PICTURE)) # Берем хеш картинки до загрузки
        self.app.upload_picture(PATH_TO_PICTURE) # Загружаем картинку
        self.app.download_picture(PICTURE_NAME) # Скачиваем картинку
        new_hesh = (md5('C:\\Download_from_mailru\\' + PICTURE_NAME)) # Берем хеш картинки после загрузки
        assert old_hesh == new_hesh # Сравниваем хеш до и после загруки
        self.app.remove_picture(PICTURE_NAME) # Удаляем картинку и чистим папку для загрузки

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
