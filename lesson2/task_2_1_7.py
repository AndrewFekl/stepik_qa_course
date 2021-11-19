from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    # Считываем Х и вычисляем значение
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Заполнение полей
    check_field = browser.find_element_by_id("robotCheckbox")
    check_field.click()
    radio_field = browser.find_element_by_id("robotsRule")
    radio_field.click()
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    # Отправка формы
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
    # Получение текста по результатам отправки формы

except Exception as ex:
    print(ex)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

