from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
import allure

from locators.main_page_locators import MainPageLocators
import data


class TestMainPage:

    driver = None

    @classmethod
    def setup_class(cls):
        # драйвер для браузера Firefox
        cls.options = Options()
        cls.options.add_argument('+headless')
        cls.driver = webdriver.Firefox(cls.options)

    @allure.title('Проверка ответов на форме "Вопросы о главном"')
    @allure.description('Проверка корректности ответов при нажатии на конкрет ный фопрос на форме "Вопросы о главном"')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_check_answer_on_all_questions(self):
        mainpage = MainPage(self.driver)
        mainpage.go_to_url(data.WEB_LINK)

        for question in mainpage.get_questions_list():
            locate_str = question.get_attribute('aria-controls')
            self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
            mainpage.wait_to_element(MainPageLocators.wait_about_rent)
#            mainpage.wait_form_about_rent()
            mainpage.click_to_element(question)
            mainpage.wait_element_by_id(locate_str)
#            mainpage.wait_questions_form(locate_str)
            assert mainpage.get_answer_text(locate_str) == data.ANSWER_ASSERT_TEXTS[int(locate_str[-1])], 'Не корректный ответ на вопрос: ' + question.text

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
