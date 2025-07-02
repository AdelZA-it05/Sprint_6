from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import allure

import data
from pages.logo_page import LogoPage
from locators.logo_page_locators import LogoPageLocators

class TestScooterLogo:

    driver = None

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Firefox
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    @allure.title('Проверка перехода при нажатии на логотип Самоката')
    @allure.description('Проверка что при нажатии на логотип самоката выполняется переход на главную страницу')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_check_click_scooter_logo(self):
        logopage = LogoPage(self.driver)
        logopage.go_to_url(data.WEB_LINK)

        # Клик по логотипу и получение текущего url
        logopage.click_to_element_locator(LogoPageLocators.logo_bike)
        logopage.wait_to_element(LogoPageLocators.logo_bike_form)

        assert self.driver.current_url == data.SCOOTER_LOGO

    @allure.title('Проверка перехода при нажатии на логотип Яндекса')
    @allure.description('Проверка что при нажатии на логотип Янекса  выполняется переход на новую вкладку и открывается яндекс-dzen')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_check_click_yandex_logo(self):
        logopage = LogoPage(self.driver)
        logopage.go_to_url(data.WEB_LINK)

        logopage.click_to_element_locator(LogoPageLocators.logo_yandex)
        logopage.wait_new_sheet_visible()
        logopage.wait_to_element(LogoPageLocators.logo_yandex_title)

        assert self.driver.current_url == data.DZEN_LOGO

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
