from selenium import webdriver
import allure

from pages.base_page import BasePage


# Класс оформления заказа
class LogoPage(BasePage):

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @allure.step("Ожидание новой вкладки")
    def wait_new_sheet_visible(self):
        window_handles_before = self.driver.window_handles
        self.driver.switch_to.window(window_handles_before[1])


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()