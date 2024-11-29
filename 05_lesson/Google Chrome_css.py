from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Откройте страницу  http://uitestingplayground.com/classattr.
driver = webdriver.Chrome()
driver.get(" http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку.
button = driver.find_element(By.CSS_SELECTOR, ".class3.btn-primary").click()

sleep(10)
