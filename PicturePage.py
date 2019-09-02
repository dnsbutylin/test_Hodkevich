
from Locators import Locator
from selenium.webdriver.common.by import By


class PicturePage():

    def __init__(self, driver):
        self.driver = driver
        self.delete_button = driver.find_elment(By.CSS_SELECTOR, Locator.delete_button)
        self.confirm_delete_button = driver.find_elment(By.XPATH, Locator.confirm_delete_button)
        self.download_button = driver.find_elment(By.XPATH, Locator.download_button)
        self.close_advertising1 = driver.find_elment(By.CSS_SELECTOR, Locator.close_advertising1)
        self.close_advertising2 = driver.find_elment(By.CSS_SELECTOR, Locator.close_advertising2)
        # Аттрибуты для проверки наличия рекламы
        self.check_advertising1 = driver.find_elements(By.CSS_SELECTOR, Locator.close_advertising1)
        self.check_advertising2 = driver.find_elements(By.CSS_SELECTOR, Locator.close_advertising2)

    def click_delete_button(self):
        self.delete_button.click()

    def click_confirm_delete_button(self):
        self.confirm_delete_button.click()

    def click_download_button(self):
        self.download_button.click()

    def click_close_advertising(self):
        if self.check_advertising1:
            self.close_advertising1.click()
        if self.check_advertising2:
            self.close_advertising2.click()


