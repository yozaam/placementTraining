# Required concepts: https://www.w3schools.com/python/python_intro.asp unpacking functions
print('Question: function to return max of all keyword arguments')

def findMax(**nums):
  val = float('-inf')
  name = ''
  for n,v in nums.items():
    if v > val:
      # if the value is smaller update the answer
      name,val = n,v
  print(name,'is biggest with value ',val)

findMax(n1=3,n4=34)
