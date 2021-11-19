from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_name("firstname").send_keys("Andrew")
    browser.find_element_by_name("lastname").send_keys("Brown")
    browser.find_element_by_name("email").send_keys("tt@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'some_bugs_repaire.txt')
    browser.find_element_by_css_selector("input[type='file']").send_keys(file_path)

    browser.find_element_by_class_name("btn.btn-primary").click()

except Exception as ex:
    print(ex)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


