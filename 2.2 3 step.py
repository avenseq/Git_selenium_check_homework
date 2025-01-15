from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum_num = num1 + num2
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{sum_num}']").click()

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:

    time.sleep(4)
    browser.quit()

