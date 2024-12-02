from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    num11 = num1.text
    num22 = num2.text
    num11 = int(num11)
    num22 = int(num22)
    summ = num11 + num22
    summ2 = str(summ)

    a = Select(browser.find_element(By.TAG_NAME, "select"))
    a.select_by_value(value=str(summ2))

    button = browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()