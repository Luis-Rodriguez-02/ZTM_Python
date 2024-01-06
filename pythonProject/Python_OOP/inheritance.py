# - Encapsulation -> grant more functionality
# - Abstraction -> hide away unecessary things
# - Inheritance -> inherit functionality from other objects


# Users -> Can be wizards or archers -> they must be signed in
class User():
  def sign_in(self):
    print('Logged in')
  
class Wizard(User):  # Passing the parent class into parameters of child classes
  def __init__(self, name, power) -> None:
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows) -> None:
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'Attacking with {self.num_arrows} arrows')

wizard1 = Wizard('Luis', 'Fire')
wizard1.sign_in()
wizard1.attack()

archer1 = Archer('Robin', 500)
archer1.attack()

is_wizard = isinstance(wizard1, Wizard)  # we give it the (instance, class)
print(is_wizard)

# isinstance -> tells us if an instance is part of a class

# Everything in object inherits from the base class in python -> this is why we have the auto dunder methods

wizard1.__repr__
[].__repr__


