import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

link_list = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('pytest', link_list)
def test_find_message_and_check_feedback(browser, pytest):

    browser.implicitly_wait(10)

    secret_message = ''

    link = pytest
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(answer))
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    button.click()

    feedback_optional = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))).text

    if feedback_optional != "Correct!":
        secret_message += feedback_optional
    print(secret_message)
    #sys.stdout.write(secret_message)

    assert feedback_optional == 'Correct!', f"Exstra message is '{feedback_optional}', should be 'Correct!'"









