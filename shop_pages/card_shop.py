import allure
from selenium.webdriver.common.by import By

class Card:
  """Класс для работы с корзиной"""

  def __init__(self, driver):
      self._driver = driver
  
  @allure.step("Кликнуть checkout")
  def clic_checkout (self) -> None:
    self._driver.find_element(By.ID, "checkout").click()
