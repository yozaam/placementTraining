# Required concepts: https://www.w3schools.com/python/python_intro.asp while loops and lists

print('Question: Reverse a list without inbuilt function/slicing')

li = [1,2,3,4,5]
# we need to make the first element the last
# and then keep swapping them :D
left, right = 0, len(li)-1

while left < right:
  li[left],li[right] = li[right],li[left]
  left +=1
  right -=1

#single line
li = [1,2,3,4,5]
for left in range(len(li)//2):
  li[left],li[len(li)-left-1] = li[len(li)-left-1],li[left] 

print('Answer:')
print(li)