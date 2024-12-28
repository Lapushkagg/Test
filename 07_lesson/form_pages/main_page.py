from selenium.webdriver.common.by import By

class MainPage:

  form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
       }

  def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

  def fill_fields(self, form_data):
    for field, value in form_data.items():
        self._driver.find_element(By.CSS_SELECTOR,
                            f"[name={field}]").send_keys(value)
  

  def click_Submit(self):
    self._driver.find_element(By.CSS_SELECTOR,
                        "button[type=submit]").click()
    
  def check_fields (self, form_data):

    for field_id in list(form_data.keys()):
        assert ("alert-success" in self._driver.find_element(
            By.ID, field_id).get_attribute("class"))
        
  def check_zip (self):
    assert ("alert-danger" in self._driver.find_element(
        By.ID, 'zip-code').get_attribute("class"))
    