import allure
from selenium.webdriver.common.by import By


class MainPage:
    """Класс для работы с главной страницей почтовой формы"""

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
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    @allure.step("Заполнить поля значениями")
    def fill_fields(self, form_data: dict) -> None:
        for field, value in form_data.items():
            element = self._driver.find_element(
                By.CSS_SELECTOR, f"[name={field}]"
            )
            element.clear()  # Очищаем поле перед вводом
            element.send_keys(value)

    @allure.step("Кликнуть 'Подтвердить'")
    def click_submit(self) -> None:
        self._driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]"
        ).click()

    @allure.step("Проверить заполненные поля")
    def check_fields(self, form_data: dict) -> dict:
        fields_status = {}
        for field_id in form_data.keys():
            element_class = self._driver.find_element(
                By.ID, field_id
            ).get_attribute("class")
            fields_status[field_id] = element_class
        return fields_status

    @allure.step("Проверить заполненный ZIP-код")
    def check_zip(self) -> str:
        zip_class = self._driver.find_element(
            By.ID, "zip-code"
        ).get_attribute("class")
        return zip_class
