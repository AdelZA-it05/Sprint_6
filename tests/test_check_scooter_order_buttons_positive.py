from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import pytest
import allure

import data
from pages.scooter_positive import ScooterPositive
import locators.page_buttons_locators as locators


class TestScooterButtons:

    driver = None

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Firefox
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    @allure.title('Проверка верхней и нижней кнопки Заказать')
    @allure.description('На главной странице лве кнопки Заказать, проверяем что, обе при нажатии переходят на форму заявки на аренду самоката')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Задаём параметры для проверки верхней и нижней кнопки заказать')
    @pytest.mark.parametrize(
        'parent_locator, children_locator, button_direct',
        [
            [locators.order_button_up, locators.order_button, 'up']
            ,[locators.order_button_down, locators.order_button, 'down']]
    )
    def test_scooter_order_buttons_positive(self, parent_locator, children_locator, button_direct):
        self.driver.get(data.WEB_LINK)
        scooterpositive = ScooterPositive(self.driver)
        parent_element = self.driver.find_element(*parent_locator)
        children_element = parent_element.find_element(*children_locator)
        if button_direct == 'down':
            self.driver.execute_script("arguments[0].scrollIntoView(true);", children_element)
            scooterpositive.wait_element_visible(parent_locator)
        scooterpositive.wait_element_clickable(children_element)
        children_element.click()
        scooterpositive.wait_order_form()
        assert self.driver.find_element(*locators.order_form).text == 'Для кого самокат'

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
