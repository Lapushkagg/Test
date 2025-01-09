import allure
from selenium.webdriver.common.by import By

class MainShop:
  """Класс для работы с главной страницей магазина"""

  def __init__(self, driver):
    self._driver = driver

  @allure.step("Добавить в корзину товары")
  def add_to_card (self) -> None:
    Backpack = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    Backpack.click()
    T_Shirt = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    T_Shirt.click()
    Onesie = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    Onesie.click()

  @allure.step("Открыть корзину")
  def open_card(self) -> None:
    shopping_cart = self._driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart.click()