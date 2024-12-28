from selenium.webdriver.common.by import By

class Checkout:

  form_data3 = {
        "first-name": "Elizaveta",
        "last-name": "Sigareva",
        "postal-code": "546456",
  }
    
  def __init__(self, driver):
      self._driver = driver

  def fill_form (self, form_data3):
    for field, value in form_data3.items():
      self._driver.find_element(By.CSS_SELECTOR,
                            f"[id={field}]").send_keys(value)

  def click_Continue(self):
     self._driver.find_element(By.ID, "continue").click()