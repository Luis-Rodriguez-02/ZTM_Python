# Static methods -> use of decorators

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  @classmethod  #this is a decorator
  def adding_things(cls, num1, num2):  # first parameter is the class -> instead of self
    return cls('Teddy', num1 + num2)
  

player3 = (PlayerCharacter.adding_things(5, 10))
print(player3.name)

@staticmethod  # works the same way but we dont have access to the cls -> exactly how the Java and C++ static methods work
def adding_things2(num1, num2):
  return num1 + num2