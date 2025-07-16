from selenium.webdriver.common.by import By

class ButtonPageLocators:
    # Parent верхней Кнопки заказать
    order_button_up = [By.CLASS_NAME, 'Header_Nav__AGCXC']
    # Parent нижней Кнопки заказать
    order_button_down = [By.CLASS_NAME, 'Home_FinishButton__1_cWm']
    # Кнопка заказать (children)
    order_button = [By.XPATH, "//button[text()='Заказать']"]
    # Форма Оформление заказа Для кого самокат
    order_form = [By.CLASS_NAME, 'Order_Header__BZXOb']
