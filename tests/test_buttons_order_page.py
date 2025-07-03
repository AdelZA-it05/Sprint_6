from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import pytest
import allure

import data
from pages.button_page import ButtonPage
from locators.buttons_page_locators import ButtonPageLocators as locators
# Без этого импорта не видит фикстуру драйвер
from conftest import driver


class TestButtonPage:

    driver = None

    @allure.title('Проверка верхней и нижней кнопки Заказать')
    @allure.description('На главной странице lве кнопки Заказать, проверяем что, обе при нажатии переходят на форму заявки на аренду самоката')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Задаём параметры для проверки верхней и нижней кнопки заказать')
    @pytest.mark.parametrize(
        'parent_locator, children_locator, button_direct',
        [
            [locators.order_button_up, locators.order_button, 'up']
            ,[locators.order_button_down, locators.order_button, 'down']]
    )
    def test_scooter_order_buttons_positive(self, driver, parent_locator, children_locator, button_direct):
        buttonpage = ButtonPage(driver)
        buttonpage.go_to_url(data.WEB_LINK)

        parent_element = buttonpage.find_element_with_wait(parent_locator)
        children_element = parent_element.find_element(*children_locator)
        if button_direct == 'down':
            driver.execute_script("arguments[0].scrollIntoView(true);", children_element)
            buttonpage.wait_to_element(parent_locator)
        buttonpage.click_to_element(children_element)
        buttonpage.wait_to_element(locators.order_form)
        assert driver.find_element(*locators.order_form).text == 'Для кого самокат'
