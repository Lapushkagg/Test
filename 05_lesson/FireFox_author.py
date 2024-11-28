from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService

# Откройте страницу http://the-internet.herokuapp.com/login.
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith.
username ="#username"
userNameField = driver.find_element(By.CSS_SELECTOR, username)
userNameField.send_keys("tomsmith")

# В поле password введите значение SuperSecretPassword!.
password = "#password"
passwordField = driver.find_element(By.CSS_SELECTOR, password)
passwordField.send_keys("SuperSecretPassword!")

# Нажмите кнопку Login.
button = driver.find_element(By.CSS_SELECTOR, "#login button").click()
sleep(5)