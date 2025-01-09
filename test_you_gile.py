import requests
from auth_id import auth_company_id
from projects import projects


api =auth_company_id("https://ru.yougile.com") 
token = "IIhLYdyFesKnUVD6Wk7CqYhWOxzelwl5ybI1dSGGLgljXZmOwi9ADRfTn+QCNh7f"
api2=projects("https://ru.yougile.com") 
par = {'Authorization':f'Bearer {token}'}


def test_auth():
  token = api.get_token()

def test_get_progects():
  body = api2.get_progects(par)
  assert len(body) > 0

def test_add_project():
    # Получить количество проектов до
  body = api2.get_progects(par)
  len_before = len(body) # Находим длину переменной

    # Создать новую компанию
  name = "ГосУслуги"
  api2.create_progect(par, name)

    # Получить количество проектов после
  body2 = api2.get_progects(par)
  len_after = len(body2) # Находим длину переменной

    # Проверить, что размер списка увеличен на +1
  assert len_after - len_before == 1
    # Проверить название и описание
  assert body[-1]["title"] == name

def test_get_one_company():
    name = "VS Code"
    new_id = api2.create_progect(par, name)["id"]
    new_company = api2.get_progect(new_id,par)
    assert new_company['title'] == name

def test_edit_one_company():
    name = "Compant to edited"
    new_id = api2.create_progect(par, name)["id"]
    new_name = "updated"
    api2.edit(par, new_id, new_name)
    edit = api2.get_progect(new_id,par)
    assert edit['title'] == new_name

def test_delete_one_company():
    name = "Compant to delete"
    new_id = api2.create_progect(par, name)["id"]
    #     #Получаем список компаний и сохраняем его длинну
    body = api2.get_progects(par)
    len_before = len(body)
    new_name = "updated"
    delete = True
    api2.edit(par, new_id, new_name, delete)
        # Проверяем что спсок компаний меньше на 1
    body2 = api2.get_progects(par)
    len_after = len(body2)
    assert len_before- len_after == 1




