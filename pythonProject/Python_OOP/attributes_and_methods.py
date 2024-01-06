# OOP allows us to create objects that have 
# - methods 
# - attributes


class PlayerCharacter:
  membership = True  # Class object attribute -> belongs to the class (static)
  def __init__(self, name, age):
    if (self.membership or PlayerCharacter.membership):
      self.name = name  # instance / attribute 
      self. age = age
  
  def shout(self):
    print(f'My name is {self.name}!')
  
  def run(self):
    print(f'{self.name} is running!')


player1 = PlayerCharacter('Luis', 21)
player1.shout()
player1.run().shout()