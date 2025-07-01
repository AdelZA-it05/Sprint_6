from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.page_enter_data_locators as locators
from random import randint


# Класс оформления заказа
class ScooterOrder:

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

    # Ожидание открытия формы Для кого самокат
    def wait_order_form(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locators.order_form))

    # Заполнение полей (объединить)
    def set_name(self, name_cust):
        self.driver.find_element(*locators.customer_name).send_keys(name_cust)
    def set_last_name(self, last_name_cust):
        self.driver.find_element(*locators.customer_last_name).send_keys(last_name_cust)
    def set_addres(self, address_cust):
        # На форме контроль ввода, периодически срабатывает контроль на fake-данные
        if '/' in address_cust: address_cust = address_cust.replace('/', '')
        if '(' in address_cust: address_cust = address_cust.replace('(', '')
        if ')' in address_cust: address_cust = address_cust.replace(')', '')
        if 'п.' in address_cust: address_cust = address_cust.replace('п.', '')
        if 'д.' in address_cust: address_cust = address_cust.replace('д.', '')
        if 'г.' in address_cust: address_cust = address_cust.replace('д.', '')
        if 'к.' in address_cust: address_cust = address_cust.replace('д.', '')
        if 'клх ' in address_cust: address_cust = address_cust.replace('клх ', '')
        if 'ст. ' in address_cust: address_cust = address_cust.replace('ст. ', '')

        self.driver.find_element(*locators.customer_addres).send_keys(address_cust)
    def set_station(self, num_station = None):
        self.driver.find_element(*locators.click_customer_station).click()
        scrollable_div = self.driver.find_element(*locators.parent_customer_station)
        elements_to_select = scrollable_div.find_elements(*locators.customer_station)
        number_station = randint(0, len(elements_to_select)-1)
        if num_station:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_to_select[num_station])
            self.wait_element_clickable(elements_to_select[num_station])
            elements_to_select[num_station].click()
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_to_select[number_station])
            self.wait_element_clickable(elements_to_select[number_station])
            elements_to_select[number_station].click()
    def set_phone(self, phone_cust):
        # На форме контроль ввода, периодически срабатывает контроль на fake-данные
        if ' ' in phone_cust: phone_cust = phone_cust.replace(' ', '')
        if '-' in phone_cust: phone_cust = phone_cust.replace('-', '')
        if '(' in phone_cust: phone_cust = phone_cust.replace('(', '')
        if ')' in phone_cust: phone_cust = phone_cust.replace(')', '')

        self.driver.find_element(*locators.customer_phone).send_keys(phone_cust)

    def set_order_fields(self, name_cust, last_name_cust, address_cust, phone_cust, num_station):
        self.set_name(name_cust)
        self.set_last_name(last_name_cust)
        self.set_addres(address_cust)
        self.set_station(num_station)
        self.set_phone(phone_cust)

    # Клик по кнопке "Далее"
    def click_next_button(self):
        self.driver.find_element(*locators.order_button_next).click()

    # Ожидание открытия формы Про аренду
    def wait_form_about_rent(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locators.form_about_rent))

    # Заполнение полей (объединить)
    def set_rent_time(self, date_start_rent):
        self.driver.find_element(*locators.start_rent_time).send_keys(date_start_rent)
        self.driver.find_element(*locators.start_rent_time).click()
        self.wait_element_visible([By.CLASS_NAME, 'react-datepicker-popper'])
        self.wait_element_clickable([By.CLASS_NAME, 'react-datepicker-popper'])
        self.driver.find_element(*[By.CLASS_NAME, 'react-datepicker-popper']).click()
    def set_duration_rent(self, num_duration_rent=None):
        self.wait_element_clickable(self.driver.find_element(*locators.duration_rent))
        self.driver.find_element(*locators.duration_rent).click()
        scrollable_div = self.driver.find_element(*locators.parent_duration_rent)
        elements_to_select = scrollable_div.find_elements(*locators.duration_time)
        if num_duration_rent:
            rent_duration = num_duration_rent
        else:
            rent_duration = randint(0, len(elements_to_select) - 1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_to_select[rent_duration])
        self.wait_element_clickable(elements_to_select[rent_duration])
        elements_to_select[rent_duration].click()
    def set_bike_color(self, num_color=None):
        if num_color:
            is_color = num_color
        else:
            is_color = randint(1, 2)
        if is_color == 1:
            self.driver.find_element(*locators.bike_color_grey).click()
        elif is_color == 2:
            self.driver.find_element(*locators.bike_color_black).click()
    def set_comment(self, comment):
        self.driver.find_element(*locators.courier_comment).send_keys(comment)

    def set_rent_fields(self, date_start_rent, num_duration_rent, num_color, comment):
        self.set_rent_time(date_start_rent)
        self.set_duration_rent(num_duration_rent)
        self.set_bike_color(num_color)
        self.set_comment(comment)

    # Клик по кнопке заказать
    def click_bike_order(self):
        self.driver.find_element(*locators.order_bike_button).click()

    # Ожидание формы вопроса Хотите оформить заказ
    def wait_form_question_rent(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locators.wait_order_bike))

    # Клик Да на форме Хотоите оформить заказ
    def click_bike_order_yes(self):
        self.driver.find_element(*locators.order_bike_yes).click()

    # Ожидание открытия формы: Заказ оформлен
    def wait_form_want_order_bike(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locators.wait_form_order_placed))

    # Подтверждение оформления заказа
    def get_order_placed_status(self):
        return self.driver.find_element(*locators.order_placed).text

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
