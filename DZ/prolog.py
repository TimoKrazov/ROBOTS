from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.istu.edu/")
driver.implicitly_wait(10)
class_button = driver.find_element(By.CLASS_NAME, "left")
button = class_button.find_element(By.TAG_NAME, "button")
class_button.click()
driver.quit()