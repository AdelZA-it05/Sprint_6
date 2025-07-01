from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import allure

import data
from pages.scooter_questions import ScooterQuestions


class TestScooterQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Firefox
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    @allure.title('Проверка корректности ответов на вопросы')
    @allure.description('В блоке Вопросы о важном проверяем соответствие вопросов и корректных ответов')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @allure.step('Сохраняем вопросы в список и сравниваем с ответами в data.py ')
    def test_check_answer_on_all_questions(self):

        self.driver.get(data.WEB_LINK)
        scooterquestions = ScooterQuestions(self.driver)

        for question in scooterquestions.get_questions_list():
            locate_str = question.get_attribute('aria-controls')
            self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
            scooterquestions.wait_form_about_rent()
            question.click()
            scooterquestions.wait_questions_form(locate_str)
            assert scooterquestions.get_answer_text(locate_str) == data.ANSWER_ASSERT_TEXTS[int(locate_str[-1])], 'Не корректный ответ на вопрос: ' + question.text

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
