from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.get("http://uitestingplayground.com/textinput")
input=driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.send_keys("SkyPro")
input=driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
resalt=driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(resalt)

driver.quit()