from selenium import webdriver
from selenium.webdriver.common.by import By

# Откройте страницу
driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполните форму значениями:
First_name = driver.find_element(By.NAME, "first-name")
First_name.send_keys("Иван")

Last_name = driver.find_element(By.NAME, "last-name")
Last_name.send_keys("Петров")

Address = driver.find_element(By.NAME, "address")
Address.send_keys("Ленина, 55-3")

Email = driver.find_element(By.NAME, "e-mail")
Email.send_keys("test@skypro.com")

Phone_number = driver.find_element(By.NAME, "phone")
Phone_number.send_keys("+7985899998787")

City = driver.find_element(By.NAME, "city")
City.send_keys("Москва")

Country = driver.find_element(By.NAME, "country")
Country.send_keys("Россия")

Job_position = driver.find_element(By.NAME, "job-position")
Job_position.send_keys("QA")

Company = driver.find_element(By.NAME, "company")
Company.send_keys("SkyPro")

# нажать Submit
Submit = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

# провенрка красного поля
EmptyFirstName = driver.find_element(By.ID, "zip-code")
assert EmptyFirstName.get_attribute('class').split().count('alert-danger') > 0
print('Поле Zip code не за заполнено')


def CheckAlertSuccess(field):
    assert field.split().count('alert-success') > 0


# проверка зеленых полей
FilledFirstName = driver.find_element(By.ID, "first-name")
FirstNameClasses = FilledFirstName.get_attribute('class')
CheckAlertSuccess(FirstNameClasses)
FilledLastName = driver.find_element(By.ID, "last-name")
LastNameClasses = FilledLastName.get_attribute('class')
CheckAlertSuccess(LastNameClasses)
FilledAddress = driver.find_element(By.ID, "address")
AddressClasses = FilledAddress.get_attribute('class')
CheckAlertSuccess(AddressClasses)
FilledEmail = driver.find_element(By.ID, "e-mail")
EmailClasses = FilledEmail.get_attribute('class')
CheckAlertSuccess(EmailClasses)
FilledPhoneNumber = driver.find_element(By.ID, "phone")
PhoneNumberClasses = FilledPhoneNumber.get_attribute('class')
CheckAlertSuccess(PhoneNumberClasses)
FilledCity = driver.find_element(By.ID, "city")
CityClasses = FilledCity.get_attribute('class')
CheckAlertSuccess(CityClasses)
Filled_Country = driver.find_element(By.ID, "country")
CountryClasses = Filled_Country.get_attribute('class')
CheckAlertSuccess(CountryClasses)
Filled_Job_position = driver.find_element(By.ID, "job-position")
JobpositionClasses = Filled_Job_position.get_attribute('class')
CheckAlertSuccess(JobpositionClasses)
Filled_Company = driver.find_element(By.ID, "company")
CompanyClasses = Filled_Company.get_attribute('class')
CheckAlertSuccess(CompanyClasses)
print('Остальные поля заполнены')
