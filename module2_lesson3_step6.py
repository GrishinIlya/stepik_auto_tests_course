from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

# Формула
def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Нажать кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()   
    
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Считать значение для x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Записываем ответ
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()