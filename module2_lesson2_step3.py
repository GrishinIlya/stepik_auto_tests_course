from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

# Формула
def calc(x, y):
  return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Считать значение для x и y
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    s = calc(x, y)

    # Выбираем значение из выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()