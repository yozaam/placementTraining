# Required concepts: https://www.w3schools.com/python/python_intro.asp lists

print('Question: simulate game where raj can pick the chocolate from either edge of list, he will always pick the bigger one')

chocolates = [1,3,4,5,6]

while len(chocolates) > 1:
  #check who is bigger first or last?
  if chocolates[0] > chocolates[-1]:
    # what if first is bigger?
    eat = chocolates.pop(0)
  else:
    eat = chocolates.pop()
  print('Eating ',eat)

print('Answer:')
print('Left with chocolate',chocolates[0])

