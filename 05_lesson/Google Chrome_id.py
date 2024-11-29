from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Откройте страницу http://uitestingplayground.com/dynamicid.
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку.
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
