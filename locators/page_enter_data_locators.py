from selenium.webdriver.common.by import By

# Parent верхней Кнопки заказать
order_button_up = [By.CLASS_NAME, 'Header_Nav__AGCXC']
# Parent нижней Кнопки заказать
order_button_down = [By.CLASS_NAME, 'Home_FinishButton__1_cWm']
# Кнопка заказать (children)
order_button = [By.XPATH, "//button[text()='Заказать']"]

# Форма Оформление заказа Для кого самокат
order_form = [By.CLASS_NAME, 'Order_Header__BZXOb']

# Оформление заказа имя
customer_name = [By.XPATH, '//input[@placeholder="* Имя"]']
# Оформление заказа фамилия
customer_last_name = [By.XPATH, '//input[@placeholder="* Фамилия"]']
# Оформление заказа адрес
customer_addres = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
# Оформление заказа станция метро
click_customer_station = [By.XPATH, '//input[@placeholder="* Станция метро"]']
parent_customer_station = [By.XPATH, '//div[@class=""]']
customer_station = [By.CLASS_NAME, 'Order_Text__2broi']
# Оформление заказа номер телефона
customer_phone = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']

# Копка "Далее"
order_button_next = [By.XPATH, "//button[text()='Далее']"]

# Форма Про аренду
form_about_rent = [By.XPATH, '//div[@class="Order_Header__BZXOb"]']

# Про аренду Когда привезти самокат
start_rent_time = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
# Про аренду Срок аренды
duration_rent = [By.CLASS_NAME, 'Dropdown-placeholder']
parent_duration_rent = [By.CLASS_NAME, 'Dropdown-menu']
duration_time = [By.CLASS_NAME, 'Dropdown-option']
# Про аренду Цвет самоката
bike_color = [By.CLASS_NAME, 'Order_Title__3EKne']
#   чёрный жемчуг
bike_color_black = [By.XPATH, '//input[@id="black"]']
#   серая безысходность
bike_color_grey = [By.XPATH, '//input[@id="grey"]']

# Про аренду Комментарий курьера
courier_comment = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
# Про аренду Заказать
order_bike_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

# Форма Хотите офоормить заказ
wait_order_bike = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
# Кнопка Да на форме Хотите оформить заказ
order_bike_yes = [By.XPATH, "//button[text()='Да']"]

# Форма завершения оформления заказа
wait_form_order_placed = [By.CLASS_NAME, 'Order_Content__bmtHS']

# Подтверждение заказ оформлен
order_placed = [By.CLASS_NAME, 'Order_Text__2broi']
