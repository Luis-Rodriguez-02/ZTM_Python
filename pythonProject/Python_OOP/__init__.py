# Constructor gets called every time we instantiate an object


class PlayerCharacter:
  def __init__(self, name='Annoymous', age=0):
    if age > 18:
      self.name = name
      self.age = age
    else:
      print("Too young")

player1 = PlayerCharacter('Luis', 15)