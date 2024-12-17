from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
      "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
      )
    # В поле ввода по локатору #delay введите значение 45.
    input_check = driver.find_element(By.ID, "delay")
    input_check.clear()
    input_check.send_keys("45")
    # Нажмите на кнопки:
    seven = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    seven.click()
    plus = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    plus.click()
    eight = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    eight.click()
    equals = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
    equals.click()
    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    assert WebDriverWait(driver, 45).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
        )
    driver.quit()
