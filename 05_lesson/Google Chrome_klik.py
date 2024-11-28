from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element.
button = driver.find_element(By.CSS_SELECTOR, ".example button")
x = 0
while x < 5:
  button.click()
  x = x + 1

# Соберите со страницы список кнопок Delete.
deletes = driver.find_elements(By.CSS_SELECTOR, "#elements .added-manually")

# Выведите на экран размер списка.
print(len(deletes))