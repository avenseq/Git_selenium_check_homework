from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, "input_value").text)
    res = str(calc(x))
    window = browser.find_element(By.CSS_SELECTOR, "#answer")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", 
window)
    window.send_keys(res)

    rad = browser.find_element(By.ID, "robotsRule")
    rad.click()

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


finally:
    time.sleep(4)
    browser.quit()





