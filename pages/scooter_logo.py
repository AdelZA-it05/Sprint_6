from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.page_logo_locators as locators


# Класс оформления заказа
class ScooterLogo:

    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    # Ожидание  видимости элемента
    def wait_element_visible(self, element_locator):
        # element = self.driver.find_element(*element_locator)
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(element_locator))

        # Ожидание новой вкладки
    def wait_new_sheet_visible(self):
        window_handles_before = self.driver.window_handles
        self.driver.switch_to.window(window_handles_before[1])

    # Ожидание кликабельностиэлемента
    def wait_element_clickable(self, element_locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(element_locator))

    def scooter_logo_click(self):
        self.driver.find_element(*locators.logo_bike).click()

    def get_scooter_main_page_url(self):
        return self.driver.current_url

    def yandex_logo_click(self):
        self.driver.find_element(*locators.logo_yandex).click()



    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
