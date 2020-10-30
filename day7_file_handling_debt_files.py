# Required concepts: https://www.w3schools.com/python/python_file_handling.asp file handling
import os

print('Question: Find money owed to friends')

def update_file(name, amount):
  path = 'tmp/' + name + '.txt'
  # get current amount
  reader = open(path, 'r')
  current_amount = int('0'+reader.read())
  # write the new amount
  writer = open(path, 'w')
  writer.write(str(current_amount + amount))

names = ['raj', 'riya', 'raj']
amounts = [1000, 200, 300]

# # first make empty files for all :)
for name in names:
  open('tmp/'+name+'.txt','w')

for name, amount in zip(names, amounts):
  update_file(name, amount)

print('Made the files with total debts')
