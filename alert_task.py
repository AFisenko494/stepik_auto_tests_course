from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    ans = calc(x)
    

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(ans)

    submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit.click()



finally:
    time.sleep(10)
    browser.quit()