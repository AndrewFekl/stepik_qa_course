from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    inputs = browser.find_elements_by_css_selector("input:required")
    first_name = "Ivan"
    last_name = "Ivanov"
    email = "ya@ya.ru"

    for input in inputs:
        placeholder = input.get_attribute("placeholder")
        if "first" in placeholder:
            input.send_keys(first_name)
        elif "last" in placeholder:
            input.send_keys(last_name)
        elif "email" in placeholder:
            input.send_keys(email)
        else:
            break

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


