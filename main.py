# Required concepts: https://www.w3schools.com/python/python_intro.asp Everything till for loops

print('Question: count occurance of 2 in a number')

number = '222222222223456'
count = 0

# go through all the digits, check if it is 2
for digit in number:
  if digit == '2':
    count += 1

# single line
count = len(number) - len(number.replace('2',''))

print('Answer:')
print('2 has ',count,'occurances')

#If you are same as your reverse, you are a palindrome
