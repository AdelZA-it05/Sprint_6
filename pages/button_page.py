from selenium import webdriver
import allure

from pages.base_page import BasePage
from locators.buttons_page_locators import ButtonPageLocators


# Класс Проверки кнопок Заказать
class ButtonPage(BasePage):

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()