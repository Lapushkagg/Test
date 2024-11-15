class User:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def print_name(self):
    print(self.first_name)

  def print_Suname(self):
    print(self.last_name)

  def print_FIO(self):
    print(self.first_name, self.last_name)