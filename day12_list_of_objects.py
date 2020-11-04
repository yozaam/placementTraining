# Required concepts: https://www.w3schools.com/python/python_intro.asp OOPS & list comprehension

print('Question: Make a list of objects with different properties')

class Bird:
  def __init__(self,name,color):
    # this constructor creates a Bird with name
    self.name = name
    self.color = color

all_names = ['parrot', 'ostrich']
all_colors = ['green', 'blue']
# n: no. of birds
n = len(all_names)

all_birds = [Bird(all_names[i],all_colors[i]) for i in range(n)]

for bird in all_birds:
  print(bird.name, bird.color)
