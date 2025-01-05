import requests
from auth_id import auth_company_id
from projects import projects


api =auth_company_id("https://ru.yougile.com") 
api2=projects("https://ru.yougile.com") 

def test_auth():
  token = api.get_token()
  print(token)

def test_get_progects():
  body = api2.get_progects()
  assert len(body) > 0

def test_add_project():
    # Получить количество проектов до
  body = api2.get_progects()
  len_before = len(body) # Находим длину переменной

    # Создать новую компанию
  name = "ГосУслуги"
  api2.create_progect(name)

    # Получить количество проектов после
  body = api2.get_progects()
  len_after = len(body) # Находим длину переменной

    # Проверить, что размер списка увеличен на +1
  assert len_after - len_before == 1
    # Проверить название и описание
  assert body[-1]["title"] == name

def test_get_one_company():
    name = "VS Code"
    new_id = api2.create_progect(name)["id"]
    new_company = api2.get_progect(new_id)
    assert new_company['name'] == name

def test_edit_one_company():
    name = "Compant to edited"
    new_id = api2.create_progect(name)["id"]
    new_name = "updated"
    edit = api2.edit(new_id, new_name)
    assert edit['name'] == new_name

def test_delete_one_company():
    name = "Compant to edited"
    new_id = api2.create_progect(name)["id"]
    #     #Получаем список компаний и сохраняем его длинну
    body = api2.get_progects()
    len_before = len(body)
    new_name = "updated"
    delete = True
    api2.edit(new_id, new_name, delete)
        # Проверяем что спсок компаний меньше на 1
    body2 = api2.get_progects()
    len_after = len(body2)
    assert len_before- len_after == 1




