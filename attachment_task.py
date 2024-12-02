from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    Fname = browser.find_element(By.NAME,'firstname')
    Fname.send_keys('Иванов')
    Fname = browser.find_element(By.NAME,'lastname')
    Fname.send_keys('Иван')
    email = browser.find_element(By.NAME,'email')
    email.send_keys('MAIL_22@ff.ru')

    fileObj = browser.find_element(By.NAME, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    fileObj.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME,'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()