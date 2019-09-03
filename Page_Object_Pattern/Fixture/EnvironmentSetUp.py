
import unittest
from selenium import webdriver


class EnvironmentSetUp(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()  # Меняем опции у браузера для скачивания файла в нужную директорию
        prefs = {'download.default_directory': 'C:\\Download_from_mailru\\'}  # Путь к директории для скачивания файла
        chrome_options.add_argument('--start-maximized')
        #chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(6)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()