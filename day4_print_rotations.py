# Required concepts: https://www.w3schools.com/python/python_intro.asp strings

print('Question: Print all rotations of a list')

# suboptimal is :
#
#for i in range(len(li)):
#  print(li[-i:] + lst[:-i])


# this is the optimal solution, without any extra space, since we are just printing!

li = [1,2,3,4,5,6]
n = len(li)
# for each rotation you start at the new start
for new_start in range(n):
  next_ = (new_start + 1)%n
  print('\n',li[new_start], end=' ')
  while next_ != new_start:
    print(li[next_],end=' ')
    next_ = (next_+1)%n
    # keep printing in circular fashion until you reach the start poiint :D


print('\nare all rotations, our answer')




