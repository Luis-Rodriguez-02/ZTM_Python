# Last time we overrode methods we made -> for a specific instance the method became useless -> we must not give access to modify the functions after creation

# Python has no true private variables

# We must do _name to have private variables

class PlayerCharacter:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  # The idea is to abstract the code -> they can still be modified but by using conventions we can prevent the code from being modified.
