from sqlalchemy import create_engine, inspect, text  
from sqlalchemy.exc import SQLAlchemyError

class Table:
  def __init__(self, connection_string):
    self.db = create_engine(connection_string)

  scripts = {
        "select": "select * from student",
        "select by level": "select * from student where level = :new_level",
        "delete by id": "DELETE FROM student WHERE level = :level",
        "insert new" : "insert into student(\"level\") values (:level)",
        "UPDATE" :"UPDATE student SET level = :new_level WHERE level = :old_level"
    }
  
  def create_student(self, level):
    connection = self.db.connect() 
    transaction = connection.begin()
    sql = text(self.scripts["insert new"])
    data = connection.execute(sql, {"level": level})
    transaction.commit()


  def delete_student(self, level):
    connection = self.db.connect() 
    transaction = connection.begin()
    sql = text(self.scripts["delete by id"])
    connection.execute(sql, {"level": level})
    transaction.commit()


  def edit_student(self, level, new_level):
    connection = self.db.connect() 
    transaction = connection.begin()
    sql = text(self.scripts["UPDATE"])
    connection.execute(sql, {"new_level": new_level, "old_level": level})
    transaction.commit()


  def get_student(self):
    connection = self.db.connect() 
    resalt = connection.execute(text(self.scripts["select"]))
    return resalt.mappings().all()
  
  def get_student_by(self, level):
    connection = self.db.connect() 
    sql = text(self.scripts["select by level"])
    resalt = connection.execute(sql, {"new_level": level})
    return resalt.mappings().all()