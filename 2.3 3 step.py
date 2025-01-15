from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element(By.ID, "input_value").text)
    res = str(calc(x))
    window = browser.find_element(By.CSS_SELECTOR, "#answer")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", 
window)
    window.send_keys(res)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
finally:
    time.sleep(4)
    browser.quit()
