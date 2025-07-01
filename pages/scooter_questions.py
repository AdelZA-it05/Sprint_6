from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.page_questions_locators as locators


# Класс  страницы сервиса
class ScooterQuestions:

    def __init__(self, driver):
        self.driver = driver

    # Получение списка вопросов
    def get_questions_list(self):
        # return self.driver.find_elements(*self.questions_list)
        return self.driver.find_elements(*locators.questions_list)

    def wait_form_about_rent(self):
        # WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.wait_about_rent))
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locators.wait_about_rent))

    def wait_questions_form(self, question_number):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable([By.ID, question_number]))


    # Получение текста ответа по номеру вопроса
    def get_answer_text(self, answer_text_locator):
        parent_element = self.driver.find_element(*[By.ID, answer_text_locator])
        paragraph_element = parent_element.find_element(By.TAG_NAME, "p")
        return paragraph_element.text



