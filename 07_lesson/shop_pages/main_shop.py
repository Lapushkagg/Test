from selenium.webdriver.common.by import By

class MainShop:

  def __init__(self, driver):
    self._driver = driver

  def add_to_card (self):
    Backpack = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    Backpack.click()
    T_Shirt = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    T_Shirt.click()
    Onesie = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    Onesie.click()

  def open_card(self):
    shopping_cart = self._driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart.click()