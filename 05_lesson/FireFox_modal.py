from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажмите на кнопку Сlose.
button = driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()
