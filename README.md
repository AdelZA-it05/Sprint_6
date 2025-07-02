# Yandex Practicum
#   Sprint_6 

## Структура проекта:
- locators         <локаторы>
- pages            <классы> 
- tests            <тесты>
- allure-results   <отчёты>

## Базовый класс
- BasePage 

## Список тестов
### Проверка блока Вопросы о важном 
- тест: test_check_answer_on_all_questions
- класс: MainPage
- локаторы: MainPageLocators:
### Проверка точек входа в сценарий
- тест: test_scooter_order_buttons_positive
- класс: ButtonPage
- локаторы: ButtonPageLocators
### Проерка флоу позитивного сценария 
- тест: test_enter_data_into_order_form
- класс: EnterDataPage
- локаторы: EnterDataPageLocators
### Проверка нажатия на логотип Самокат и Яндекс 
- тест: ttest_check_click_scooter_logo, test_check_click_yandex_logo
- класс: LogoPage
- локаторы: LogoPageLocators

## Данные 
- модуль data.py
