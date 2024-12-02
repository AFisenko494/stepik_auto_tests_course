from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    obj1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
    obj1.send_keys('test')
    obj2 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
    obj2.send_keys('test')
    obj3 = browser.find_element(By.XPATH, "//label[text()='Phone:']/following-sibling::input")
    obj3.send_keys('test')
    obj4 = browser.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
    obj4.send_keys('test')
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()