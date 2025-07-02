from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Получаем список ответов в список")
    def get_questions_list(self):
        # return self.driver.find_elements(*self.questions_list)
        return self.driver.find_elements(*MainPageLocators.questions_list)

    @allure.step("Ожидаем блок с вопросами")
    def wait_element_by_id(self, locator_id):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable([By.ID, locator_id]))

    @allure.step("Получаем текст ответа")
    def get_answer_text(self, answer_text_locator):
        parent_element = self.driver.find_element(*[By.ID, answer_text_locator])
        paragraph_element = parent_element.find_element(By.TAG_NAME, "p")
        return paragraph_element.text



