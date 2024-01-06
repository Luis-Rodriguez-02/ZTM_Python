# - Encapsulation - Packing information together -> increases functionality
# - Abstraction - Hiding information -> giving access only to what is necessary


# All we (the user) need to know is the use case for the things that are abstracted away -> like cameras on phones -> we dont need to know how they are coded to know their use cases

class PlayerCharacter:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
  
  def speak(self):
    print(f'My name is {self.name}')


player1 = PlayerCharacter("Luis", 15)
player1.name = '!!!'
print(player1.name)
player1.speak = "This is why private is required"
player1.speak()  # modified so not callable -> became string literal
print(player1.speak)