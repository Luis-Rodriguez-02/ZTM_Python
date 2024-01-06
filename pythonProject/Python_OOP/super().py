class User():
  def __init__(self, email) -> None:
    self.email = email
  
class Wizard(User):
  def __init__(self, name, power, email) -> None:
    super().__init__(email)  #  User.__init__(self, email) or use super -> if you use super you dont need to pass in self
    self.name = name
    self.power = power


wizard1 = Wizard("Merlin", "Dark", "Merlin@aol.com")
print(wizard1.email)
  




