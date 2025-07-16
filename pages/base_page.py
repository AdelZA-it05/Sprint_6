from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.buttons_page_locators as locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 25
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element_locator(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_to_element(self, element):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    def scroll_to_element(self, some):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", some)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

    def wait_to_element(self, element_locator):
        self.wait.until(expected_conditions.visibility_of_element_located(element_locator))

    def wait_element_to_clickable(self, element_locator):
        self.wait.until(expected_conditions.element_to_be_clickable(element_locator))

    def get_list_element(self, element_locator):
            return self.driver.find_elements(*element_locator)


