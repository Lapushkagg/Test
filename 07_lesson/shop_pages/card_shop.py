from selenium.webdriver.common.by import By

class Card:

  def __init__(self, driver):
      self._driver = driver

  def clic_checkout (self):
    self._driver.find_element(By.ID, "checkout").click()
