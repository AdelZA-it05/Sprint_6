from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
import allure
import pytest

from locators.main_page_locators import MainPageLocators
import data
# Без этого импорта не видит фикстуру драйвер
from conftest import driver


class TestMainPage:

    driver = None

    @allure.title('Проверка ответов на форме "Вопросы о главном"')
    @allure.description('Проверка корректности ответов при нажатии на конкрет ный фопрос на форме "Вопросы о главном"')
    @allure.testcase('Тест-кейс из финального задания Sprtint_6')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @pytest.mark.parametrize(
        'answer_text',
        [
            data.ANSWER_ASSERT_TEXTS
           ]
    )
    def test_check_answer_on_all_questions(self, driver, answer_text):
        mainpage = MainPage(driver)
        mainpage.go_to_url(data.WEB_LINK)

        assert mainpage.check_answer_text(answer_text)

