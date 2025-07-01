from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import allure

import data
from pages.scooter_logo import ScooterLogo
import locators.page_logo_locators as locators

class TestScooterLogo:

    driver = None

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Chrome
        # cls.driver = webdriver.Chrome()
        # драйвер для браузера Firefox
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип Самокат')
    @allure.description('На главной странице есть логотип Самокат, проверяем что, при нажатии переходит на главную страницу самоката')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Кликаем на логотип и сравниваем url')
    def test_check_click_scooter_logo(self):
        self.driver.get(data.WEB_LINK)
        scooterlogo = ScooterLogo(self.driver)
        # Клик по логотипу и получение текущего url
        scooterlogo.scooter_logo_click()
        scooterlogo.wait_element_visible(locators.logo_bike_form)
        scooterlogo.get_scooter_main_page_url()
        # Проверка
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип Яндекс')
    @allure.description('На главной странице есть Яндекс, проверяем что, при нажатии переходят на главную страницу Яндекс dzen')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Кликаем на логотип и сравниваем url')
    def test_check_click_yandex_logo(self):
        self.driver.get(data.WEB_LINK)
        scooterlogo = ScooterLogo(self.driver)
        # Клик по логотипу и получение url Yandex
        scooterlogo.yandex_logo_click()
        scooterlogo.wait_new_sheet_visible()
        scooterlogo.wait_element_visible(locators.logo_yandex_title)
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'






    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
