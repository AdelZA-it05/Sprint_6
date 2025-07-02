from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from faker import Faker
fake = Faker("ru_RU")
import pytest
import datetime
import allure

import data
from pages.enter_data_page import EnterDataPage
from locators.enter_data_page_locators import EnterDataPageLocators


class TestScooterEnterData:

    # драйвер для браузера Firefox
    driver = None

    @classmethod
    def setup_class(cls):
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    @allure.title('Заполнение формы заказа самоката')
    @allure.description('Проверка заполнения формы заказа (параметризация - два тестовых набора данных)')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Задаём параметры для проверки различных наборов данных')
    @pytest.mark.parametrize(
        'name_cust, last_name_cust, address_cust, phone_cust, num_station, date_start_rent, num_duration_rent, num_color, comment',
        [
            [fake.first_name(), fake.last_name(), fake.address(), fake.phone_number(), 1, fake.date(pattern="%d.%m.%Y"), 1, 1, fake.text()]
        , [fake.first_name().lower(), fake.last_name().lower(), fake.address(), fake.phone_number(), None, str(datetime.date.today()), None, None, '-Tекст в pазных раслladkah']]
    )
    def test_enter_data_into_order_form(self, name_cust, last_name_cust, address_cust, phone_cust, num_station, date_start_rent, num_duration_rent, num_color, comment):
        enterdatapage = EnterDataPage(self.driver)
        enterdatapage.go_to_url(data.WEB_LINK)

        # Кнопка заказать
        parent_element = enterdatapage.find_element_with_wait(EnterDataPageLocators.order_button_up)
        children_element = parent_element.find_element(*EnterDataPageLocators.order_button)
        enterdatapage.wait_element_to_clickable(children_element)
        enterdatapage.click_to_element(children_element)
        # Форма Для кого нужен самокат
        enterdatapage.wait_to_element(EnterDataPageLocators.order_form)
        # Заполнение полей
        enterdatapage.set_order_fields(name_cust, last_name_cust, address_cust, phone_cust, num_station)
        # Кнопка Далее
        enterdatapage.click_to_element_locator(EnterDataPageLocators.order_button_next)
        # Форма Про аренду
        enterdatapage.wait_to_element(EnterDataPageLocators.form_about_rent)
        # Заполнение полей
        enterdatapage.set_rent_fields(date_start_rent, num_duration_rent, num_color, comment)
        # Кнопка Заказать
        enterdatapage.click_to_element_locator(EnterDataPageLocators.order_bike_button)
        # Ожидание формы вопроса подтверждения заказа
        enterdatapage.wait_to_element(EnterDataPageLocators.wait_order_bike)
        # Клик Да на форме подтверждения заказа
        enterdatapage.click_to_element_locator(EnterDataPageLocators.order_bike_yes)
        # Ожидание формы Заказ оформлен
        enterdatapage.wait_to_element(EnterDataPageLocators.wait_form_order_placed)
        # Получение подтверждения заказа
        assert enterdatapage.get_text_from_element(EnterDataPageLocators.order_placed)[0:14] == 'Номер заказа: '


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
