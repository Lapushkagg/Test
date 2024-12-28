from selenium import webdriver
from form_pages.main_page import MainPage
from calc_pages.main_calc import MainCalc
from shop_pages.autor_page import autor
from shop_pages.main_shop import MainShop
from shop_pages.card_shop import Card
from shop_pages.checkout_shop import Checkout
from shop_pages.total_shop import Total

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

form_data2 = {
        "user-name": "standard_user",
        "password": "secret_sauce"
      }

form_data3 = {
        "first-name": "Elizaveta",
        "last-name": "Sigareva",
        "postal-code": "546456",
  }

def test_form():

    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.fill_fields(form_data)
    main_page.click_Submit()
    main_page.check_fields(form_data)
    main_page.check_zip()
    driver.quit()

def test_calc():

    driver = webdriver.Chrome()
    main_page = MainCalc(driver)
    main_page.input_timer("45")
    main_page.click_buttons()
    main_page.check_resalt("15")
    driver.quit()

def test_shop():

    driver = webdriver.Chrome()
    main_page = autor(driver)
    main_page.autor(form_data2)

    main_page = MainShop(driver)
    main_page.add_to_card()
    main_page.open_card()

    main_page = Card(driver)
    main_page.clic_checkout()

    main_page = Checkout(driver)
    main_page.fill_form(form_data3)
    main_page.click_Continue()

    main_page = Total(driver)
    resalt = main_page.cacl_total()
    driver.quit()
    main_page.check_total(resalt)
