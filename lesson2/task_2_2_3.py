from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    # вытащим числа html и найдем их сумму
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    sum = num1 + num2
    # Сделаем выбор равный сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    # Отправим форму
    browser.find_element_by_class_name("btn.btn-default").click()





except Exception as ex:
    print(ex)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
