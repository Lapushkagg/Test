import allure
from selenium.webdriver.common.by import By


class Checkout:
    """Класс для работы с формой доставки"""

    form_data3 = {
        "first-name": "Elizaveta",
        "last-name": "Sigareva",
        "postal-code": "546456",
    }

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Заполнить форму отправки")
    def fill_form(self, form_data3: dict) -> None:
        for field, value in form_data3.items():
            self._driver.find_element(
                By.CSS_SELECTOR, f"[id={field}]").send_keys(value)

    @allure.step("Кликнуть по кнопке продолжить")
    def click_Continue(self) -> None:
        self._driver.find_element(By.ID, "continue").click()
