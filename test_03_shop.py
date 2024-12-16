from selenium import webdriver
from selenium.webdriver.common.by import By

# Откройте сайт магазина: https://www.saucedemo.com/.
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
# Авторизуйтесь как пользователь standard_user.
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button").click()
# Добавьте в корзину товары:
Backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
Backpack.click()
T_Shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
T_Shirt.click()
Onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
Onesie.click()
# Перейдите в корзину.
shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart.click()
# Нажмите Checkout
Checkout = driver.find_element(By.ID, "checkout").click()
# Заполните форму своими данными:
name = driver.find_element(By.ID, "first-name")
name.send_keys("Elizaveta")
surname = driver.find_element(By.ID, "last-name")
surname.send_keys("Sigareva")
zip = driver.find_element(By.ID, "postal-code")
zip.send_keys("546456")

# Нажмите кнопку Continue.
Continue = driver.find_element(By.ID, "continue").click()

# Прочитайте со страницы итоговую стоимость ( Total ).
result = driver.find_element(By.CLASS_NAME, "summary_total_label").text.split()

# Закройте браузер.
driver.close()

# Проверьте, что итоговая сумма равна $58.29.
assert result[1] == '$58.29'
print('проверка пройдена')
