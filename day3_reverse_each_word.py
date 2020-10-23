# Required concepts: https://www.w3schools.com/python/python_intro.asp Everything till for loops

print('Question: reverse each word of string')

sentence = 'hello world how are     you'
res = ''

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

print('Answer:')
print(res)

