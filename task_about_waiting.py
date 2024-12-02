from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#29.059677770073733

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    ans = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(ans)


    submit = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()





finally:
    time.sleep(10)
    browser.quit()