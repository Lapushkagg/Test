import allure
from selenium.webdriver.common.by import By


class Autor:
    """Класс для работы со страницей авторизации"""

    form_data2 = {
        "user-name": "standard_user",
        "password": "secret_sauce"
    }

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация")
    def login(self, form_data2: dict) -> None:
        for field, value in form_data2.items():
            self._driver.find_element(
                By.CSS_SELECTOR, f"[name={field}]").send_keys(value)
        self._driver.find_element(By.ID, "login-button").click()
