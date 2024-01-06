class Toy():
  def __init__(self, color, age) -> None:
    self.color = color
    self.age = age
    self.mydict = {
    'name': 'yoyo',
    'has_pets': False}
  
  def __str__(self) -> str:  # overriding to give a nice string representation -> basically toString from Java
    return f'{self.color}'

  def __len__(self):
    return 5

  def __del__(self):
    print('deleted!')
  
  def __call__(self):  # we call functions using this dunder method
    return('yess??')
  
  def __getitem__(self, i):
    return self.mydict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())  # python docs and dunder method modifications -> modify str dunder method
print(str(action_figure))
print(len(action_figure))
#  del action_figure
print(action_figure)
print(action_figure['name'])

