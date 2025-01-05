from bd import Table

db = Table("postgresql://postgres:1@localhost:5432/QA")

def test_add_student():
    # Получить количество компаний до
    body = db.get_student()
    len_before = len(body) # Находим длину переменной

    # Создать новую компанию
    level = "new_level"
    level=db.create_student(level)

    # Получить количество компаний после
    body = db.get_student()
    len_after = len(body) # Находим длину переменной

    # Проверить, что размер списка увеличен на +1
    assert len_after - len_before == 1
    # Проверить название и описание
    db.delete_student(level)

def test_edit_student():
    # Создать новую компанию
    level = "beginer1"
    db.create_student(level)

    new_level = "edit_level"
    db.edit_student(level, new_level)

    new_student = db.get_student_by(new_level)
    assert new_student[0]['level'] == new_level
    db.delete_student(new_level)


def test_delete_student():
    # Создать новую компанию
    level = "beginer1"
    db.create_student(level)

    db.delete_student(level)

    deleted_student=db.get_student_by(level)
    assert len(deleted_student) == 0




