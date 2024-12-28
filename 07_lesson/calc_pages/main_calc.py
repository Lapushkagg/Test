from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainCalc:

  def __init__(self, driver):
      self._driver = driver
      self._driver.maximize_window()
      self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

  def input_timer(self,num):
    input_check = self._driver.find_element(By.ID, "delay")
    input_check.clear()
    input_check.send_keys(num)
  

  def click_buttons(self):
    seven = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    seven.click()
    plus = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    plus.click()
    eight = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    eight.click()
    equals = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
    equals.click()
    
  def check_resalt (self, num):
    assert WebDriverWait(self._driver, 45+1).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), num)
        )