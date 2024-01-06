class User():
  pass

class Wizard():
  def __init__(self, name, power) -> None:
    self.name = name
    self.power = power
  
  def fly(self):
    print(f'{self.name} is flying!')

class Archer():
  def __init__(self, name, arrows) -> None:
    self.name = name
    self.arrows = arrows

  def run(self):
    print(f'{self.name} ran really fast')
    

class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Wizard.__init__(self, name, power)
    Archer.__init__(self, name, arrows)

# Multiple inheritance can get really messy

hb1 = HybridBorg('borgie', 'Fire', 100)
hb1.run()
hb1.fly()



