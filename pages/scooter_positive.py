from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.page_buttons_locators as locators


# Класс Проверки кнопок Заказать
class ScooterPositive:

    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    # Ожидание  видимости элемента
    def wait_element_visible(self, element_locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(element_locator))
    # Ожидание кликабельностиэлемента
    def wait_element_clickable(self, element_locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(element_locator))

    # Ожидание открытия страницы заказа
    def wait_order_form(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locators.order_form))

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
    