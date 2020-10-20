# Required concepts: https://www.w3schools.com/python/python_intro.asp Everything till for loops

print('Question: repeat every character twice')

li = ['a' , 'b' , 'c' , 'd']
# we want ['aa' , 'bb' , 'cc' , 'dd']

for i in range(len(li)):
  li[i]  = li[i]*2
  # all elements repeat twice so *2

#single line let's repeat them again
result = [letter*2 for letter in li]

print('Answer:')
print(result)

