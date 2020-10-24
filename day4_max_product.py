# Required concepts: https://www.w3schools.com/python/python_intro.asp lists

print('Question: Maximum product of two elements in array')



li = [-7,-6,4,1,2,3,4,5,6]
li.sort()
# 5*6 or -7*-6 only those could give me the maximum
# product of the two smallest, neg*neg 
first = li[0]*li[1]
last = li[-1]*li[-2]

print('Answer:')
print(max(first,last))