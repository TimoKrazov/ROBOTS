from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

options = Options()
options.binary_location = "C:/USER_PROGRAM/firefox" 

driver = webdriver.Firefox(options=options)

driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")


ActionChains(driver)\
    .move_to_element(username)\
    .pause(1)\
    .click()\
    .pause(1)\
    .send_keys("standard_user")\
    .move_to_element(password)\
    .pause(1)\
    .click()\
    .pause(1)\
    .send_keys("secret_sauce")\
    .move_to_element(login)\
    .pause(1)\
    .click()\
    .pause(2)\
    .perform()
filter = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(filter)
select.select_by_value("lohi")
lowItem = driver.find_element(By.CLASS_NAME, "inventory_item")
add_button = lowItem.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
cart = driver.find_element(By.ID, "shopping_cart_container")

ActionChains(driver)\
    .move_to_element(add_button)\
    .pause(1)\
    .click()\
    .pause(1)\
    .move_to_element(cart)\
    .pause(1)\
    .click()\
    .pause(2)\
    .perform()

checkout = driver.find_element(By.ID, "checkout")
ActionChains(driver)\
    .move_to_element(checkout)\
    .pause(1)\
    .click()\
    .pause(10)\
    .perform()
driver.quit()