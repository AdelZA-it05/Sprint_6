from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from faker import Faker
fake = Faker("ru_RU")
import pytest
import datetime
import allure

import data
from pages.scooter_order import ScooterOrder
import locators.page_enter_data_locators as locators


class TestScooterEnterData:


    # драйвер для браузера Firefox
    driver = None

    @classmethod
    def setup_class(cls):
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    # Проверка заполнения формы заказа (параметризация - два тестовых набора данных)
    @allure.title('Заказ самоката')
    @allure.description('На странице заполняем заявку на аренду и получаем подтверждение заявки')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Задаём параметры для тестовых наборов')  # декоратор
    @pytest.mark.parametrize(
        'name_cust, last_name_cust, address_cust, phone_cust, num_station, date_start_rent, num_duration_rent, num_color, comment',
        [
            [fake.first_name(), fake.last_name(), fake.address(), fake.phone_number(), 1, fake.date(pattern="%d.%m.%Y"), 1, 1, fake.text()]
        , [fake.first_name().lower(), fake.last_name().lower(), fake.address(), fake.phone_number(), None, str(datetime.date.today()), None, None, '-Tекст в pазных раслladkah']]
    )
    def test_enter_data_into_order_form(self, name_cust, last_name_cust, address_cust, phone_cust, num_station, date_start_rent, num_duration_rent, num_color, comment):
        self.driver.get(data.WEB_LINK)
        scooterorder = ScooterOrder(self.driver)
        # Кнопка заказать
        parent_element = self.driver.find_element(*locators.order_button_up)
        children_element = parent_element.find_element(*locators.order_button)
        scooterorder.wait_element_clickable(children_element)
        children_element.click()
        # Форма Для кого нужен самокат
        scooterorder.wait_order_form()
        # Заполнение полей
        scooterorder.set_order_fields(name_cust, last_name_cust, address_cust, phone_cust, num_station)
        # Кнопка Далее
        scooterorder.click_next_button()
        # Форма Про аренду
        scooterorder.wait_form_about_rent()
        # Заполнение полей
        scooterorder.set_rent_fields(date_start_rent, num_duration_rent, num_color, comment)
        # Кнопка Заказать
        scooterorder.click_bike_order()
        # Ожидание формы вопроса подтверждения заказа
        scooterorder.wait_form_question_rent()
        # Клик Да на форме подтверждения заказа
        scooterorder.click_bike_order_yes()
        # Ожидание формы Заказ оформлен
        scooterorder.wait_form_want_order_bike()
        # Получение подтверждения заказа
        assert scooterorder.get_order_placed_status()[0:14] == 'Номер заказа: '

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
