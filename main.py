# Required concepts: https://www.w3schools.com/python/python_intro.asp OOPS & list comprehension

print('Question: Make a list of objects with different names')

class Bird:
  def __init__(self,name):
    # this constructor creates a Bird with name
    self.name = name

all_names = ['parrot', 'ostrich']

all_birds = [Bird(name) for name in all_names]

for bird in all_birds:
  print(bird.name)