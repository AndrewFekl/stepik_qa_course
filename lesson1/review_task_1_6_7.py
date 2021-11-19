from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    # Поиск элементов 
    first_name = browser.find_element_by_css_selector("div.first_class input:required")
    last_name = browser.find_element_by_css_selector("div.second_class input:required")
    email = browser.find_element_by_css_selector("div.third_class input:required")
    # Заполнение полей
    first_name.send_keys("Richard")
    last_name.send_keys("Castle")
    email.send_keys("castle@example.com")
    # Отправка формы    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Получение текста по результатам отправки формы
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
except Exception as ex:
    print(ex)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце фай
