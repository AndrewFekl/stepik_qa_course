import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_welcome_text(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    # Передадим ссылку в объект browser
    browser.get(link)
    # Код, который заполняет обязательные поля
    first_name = "Ivan"
    last_name = "Ivanov"
    email = "ya@ya.ru"

    browser.find_element(By.CLASS_NAME, "first_block .first").send_keys(first_name)
    browser.find_element(By.CLASS_NAME,"first_block .second").send_keys(last_name)
    browser.find_element(By.CLASS_NAME,"first_block .third").send_keys(email)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text

class TestWelcome(unittest.TestCase):
    def test_link1(self):
        welcome_text = get_welcome_text("http://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",\
                         "Welcome text should be 'Congratulations! You have successfully registered!'")
    def test_link2(self):
        welcome_text = get_welcome_text("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",\
                         "Welcome text should be 'Congratulations! You have successfully registered!'")

if __name__ == "__main__":
    unittest.main()

