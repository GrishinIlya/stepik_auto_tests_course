from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Формула
def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ждем пока цена не станет 100$
    wait = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
        )
    
    # Нажать кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()   
    
    # Считать значение для x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Записываем ответ
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()