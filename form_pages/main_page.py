import allure
from selenium.webdriver.common.by import By

class MainPage:
  """Класс для работы с главной страницый почтовой формы"""

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

  @allure.step("Заполнить поля значениями")
  def fill_fields(self, form_data: dict) -> None:
    for field, value in form_data.items():
        self._driver.find_element(By.CSS_SELECTOR,
                            f"[name={field}]").send_keys(value)
  
  @allure.step("Кликнуть подтвердить")
  def click_Submit(self)-> None:
    self._driver.find_element(By.CSS_SELECTOR,
                        "button[type=submit]").click()
    
  @allure.step("Проверить заполеные поля")  
  def check_fields (self, form_data: dict) -> dict:
    fields={}
    for field_id in list(form_data.keys()):
      fields[field_id] = self._driver.find_element(By.ID, field_id).get_attribute("class")
        # assert ("alert-success" in self._driver.find_element(By.ID, field_id).get_attribute("class"))
    return fields
        
  @allure.step("Проверить заполеные zip код")  
  def check_zip (self) -> any:
    zip = self._driver.find_element(By.ID, 'zip-code').get_attribute("class")
    return zip
