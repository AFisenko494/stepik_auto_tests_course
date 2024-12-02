from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'treasure')
    nnum = x_element.get_attribute('valuex')
    x = nnum
    y = calc(x)

    obj = browser.find_element(By.ID, 'answer')
    obj.send_keys(y)

    chek = browser.find_element(By.ID, 'robotCheckbox')
    chek.click()

    radiob = browser.find_element(By.ID, 'robotsRule')
    radiob.click()

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()



finally:
    time.sleep(10)
    browser.quit()