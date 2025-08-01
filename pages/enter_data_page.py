from selenium.webdriver.common.by import By
from random import randint
import allure

from locators.enter_data_page_locators import EnterDataPageLocators
from pages.base_page import BasePage



@allure.step("Класс оформления заказа")
class EnterDataPage(BasePage):

    def set_name(self, name_cust):
        self.driver.find_element(*EnterDataPageLocators.customer_name).send_keys(name_cust)
    def set_last_name(self, last_name_cust):
        self.driver.find_element(*EnterDataPageLocators.customer_last_name).send_keys(last_name_cust)
    def set_addres(self, address_cust):
        # На форме контроль ввода, периодически срабатывает контроль на fake-данные
        if '/' in address_cust: address_cust = address_cust.replace('/', '')
        if '(' in address_cust: address_cust = address_cust.replace('(', '')
        if ')' in address_cust: address_cust = address_cust.replace(')', '')
        if 'п.' in address_cust: address_cust = address_cust.replace('п.', '')
        if 'д.' in address_cust: address_cust = address_cust.replace('д.', '')
        if 'клх ' in address_cust: address_cust = address_cust.replace('клх ', '')
        if 'ст. ' in address_cust: address_cust = address_cust.replace('ст. ', '')
        if 'с. ' in address_cust: address_cust = address_cust.replace('с. ', '')
        if 'к. ' in address_cust: address_cust = address_cust.replace('к. ', '')
        if 'к ' in address_cust: address_cust = address_cust.replace('к ', '')

        self.driver.find_element(*EnterDataPageLocators.customer_addres).send_keys(address_cust)
    def set_station(self, num_station = None):
        self.driver.find_element(*EnterDataPageLocators.click_customer_station).click()
        scrollable_div = self.driver.find_element(*EnterDataPageLocators.parent_customer_station)
        elements_to_select = scrollable_div.find_elements(*EnterDataPageLocators.customer_station)
        number_station = randint(0, len(elements_to_select)-1)
        if num_station:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_to_select[num_station])
            self.wait_element_to_clickable(elements_to_select[num_station])
            elements_to_select[num_station].click()
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_to_select[number_station])
            self.wait_element_to_clickable(elements_to_select[number_station])
            elements_to_select[number_station].click()
    def set_phone(self, phone_cust):
        # На форме контроль ввода, периодически срабатывает контроль на fake-данные
        if ' ' in phone_cust: phone_cust = phone_cust.replace(' ', '')
        if '-' in phone_cust: phone_cust = phone_cust.replace('-', '')
        if '(' in phone_cust: phone_cust = phone_cust.replace('(', '')
        if ')' in phone_cust: phone_cust = phone_cust.replace(')', '')
        self.driver.find_element(*EnterDataPageLocators.customer_phone).send_keys(phone_cust)

    @allure.step('Заполнение полей формы "Для кого самокат"')
    def set_order_fields(self, name_cust, last_name_cust, address_cust, phone_cust, num_station):
        self.set_name(name_cust)
        self.set_last_name(last_name_cust)
        self.set_addres(address_cust)
        self.set_station(num_station)
        self.set_phone(phone_cust)

    # Заполнение полей (объединить)
    def set_rent_time(self, date_start_rent):
        self.driver.find_element(*EnterDataPageLocators.start_rent_time).send_keys(date_start_rent)
        self.driver.find_element(*EnterDataPageLocators.start_rent_time).click()
        self.wait_to_element([By.CLASS_NAME, 'react-datepicker-popper'])
        self.wait_element_to_clickable([By.CLASS_NAME, 'react-datepicker-popper'])
        self.driver.find_element(*[By.CLASS_NAME, 'react-datepicker-popper']).click()
    def set_duration_rent(self, num_duration_rent=None):
        self.wait_element_to_clickable(self.driver.find_element(*EnterDataPageLocators.duration_rent))
        self.driver.find_element(*EnterDataPageLocators.duration_rent).click()
        scrollable_div = self.driver.find_element(*EnterDataPageLocators.parent_duration_rent)
        elements_to_select = scrollable_div.find_elements(*EnterDataPageLocators.duration_time)
        if num_duration_rent:
            rent_duration = num_duration_rent
        else:
            rent_duration = randint(0, len(elements_to_select) - 1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_to_select[rent_duration])
        self.wait_element_to_clickable(elements_to_select[rent_duration])
        elements_to_select[rent_duration].click()
    def set_bike_color(self, num_color=None):
        if num_color:
            is_color = num_color
        else:
            is_color = randint(1, 2)
        if is_color == 1:
            self.driver.find_element(*EnterDataPageLocators.bike_color_grey).click()
        elif is_color == 2:
            self.driver.find_element(*EnterDataPageLocators.bike_color_black).click()
    def set_comment(self, comment):
        self.driver.find_element(*EnterDataPageLocators.courier_comment).send_keys(comment)

    @allure.step('Заполнение полей формы "Про аренду"')
    def set_rent_fields(self, date_start_rent, num_duration_rent, num_color, comment):
        self.set_rent_time(date_start_rent)
        self.set_duration_rent(num_duration_rent)
        self.set_bike_color(num_color)
        self.set_comment(comment)

    def get_order_placed_status(self):
        return self.driver.find_element(*EnterDataPageLocators.order_placed).text
