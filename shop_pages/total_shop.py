import allure
from selenium.webdriver.common.by import By


class Total:
    """Класс для работы с итоговой суммой"""

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Вернуть итоговую стоимость")
    def calc_total(self) -> None:
        result = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text.split()
        return result
