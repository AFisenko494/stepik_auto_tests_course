from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/find_xpath_form")
    oj1 = browser.find_element(By.NAME, 'first_name')
    oj1.send_keys('Сергей')
    oj2 = browser.find_element(By.NAME, 'last_name')
    oj2.send_keys('Сергеев')
    oj3 = browser.find_element(By.NAME, 'firstname')
    oj3.send_keys('Москва')
    oj4 = browser.find_element(By.ID, 'country')
    oj4.send_keys('РФ')
    #elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла