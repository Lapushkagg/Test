from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService

# Откройте страницу http://the-internet.herokuapp.com/inputs.
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Введите в поле текст 1000.
driver = driver.find_element(By.CSS_SELECTOR, ".example input")
driver.send_keys("1000")
sleep(2)
# Очистите это поле (метод clear).
driver.clear()
# Введите в это же поле текст 999.
driver.send_keys("999")
sleep(5)
