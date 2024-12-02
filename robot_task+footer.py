from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.ID, 'input_value')
    x = a.text
    xx = calc(x)

    obj = browser.find_element(By.ID, 'answer')
    obj.send_keys(xx)

    chek = browser.find_element(By.ID, 'robotCheckbox')
    chek.click()

    radiob = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiob)
    radiob.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(10)
    browser.quit()