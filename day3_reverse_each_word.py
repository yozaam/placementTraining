# Required concepts: https://www.w3schools.com/python/python_intro.asp strings and slicing

print('Question: reverse each word of string')

sentence = 'hello world how are     you'
res = ''

for word in sentence.split():
  # get each word from the split function
  res += word[::-1]+" "
  #add the reverse of it

print('Answer:')
print(res)

"""
# what to reverse?
# reverse upto the space
left = 0
while left < len(sentence):
  right = sentence.find(' ',left)
  if right == -1:
    right = len(sentence)
  word = sentence[left:right]
  # now add this reversed word to result!
  print(res)
  res += word[::-1]
  left = right
  #now start from here
"""


