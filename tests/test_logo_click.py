from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import allure

import data
from pages.logo_page import LogoPage
from locators.logo_page_locators import LogoPageLocators
# Без этого импорта не видит фикстуру драйвер
from conftest import driver

class TestScooterLogo:

    driver = None


    @allure.title('Проверка перехода при нажатии на логотип Самоката')
    @allure.description('Проверка что при нажатии на логотип самоката выполняется переход на главную страницу')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_check_click_scooter_logo(self, driver):
        logopage = LogoPage(driver)
        logopage.go_to_url(data.WEB_LINK)

        # Клик по логотипу и получение текущего url
        logopage.click_to_element_locator(LogoPageLocators.logo_bike)
        logopage.wait_to_element(LogoPageLocators.logo_bike_form)

        assert logopage.get_current_url() == data.SCOOTER_LOGO

    @allure.title('Проверка перехода при нажатии на логотип Яндекса')
    @allure.description('Проверка что при нажатии на логотип Янекса  выполняется переход на новую вкладку и открывается яндекс-dzen')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_check_click_yandex_logo(self, driver):
        logopage = LogoPage(driver)
        logopage.go_to_url(data.WEB_LINK)

        logopage.click_to_element_locator(LogoPageLocators.logo_yandex)
        logopage.wait_new_sheet_visible()
        logopage.wait_to_element(LogoPageLocators.logo_yandex_title)

        assert logopage.get_current_url() == data.DZEN_LOGO

