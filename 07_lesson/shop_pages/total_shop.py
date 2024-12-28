from selenium.webdriver.common.by import By

class Total:
   
  def __init__(self, driver):
      self._driver = driver

  def cacl_total (self):
    result = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text.split()
    return result


  def check_total(self,result):
    assert result[1] == '$58.29'
