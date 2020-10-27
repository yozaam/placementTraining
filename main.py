# Required concepts: https://www.w3schools.com/python/python_intro.asp while loop and maths 
print('Question: reverse number without using strings')

def getReverse(num):
  res = 0
  while num > 0:
    # take last digit and put in the front of res
    digit = num%10
    num //=10
    res = res*10 + digit
  return res
print(getReverse(1234))
