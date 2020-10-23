# Required concepts: https://www.w3schools.com/python/python_intro.asp strings

print('Question: for sets A and B return all pairs {A(i) , B(-i)}')


l1 = ["hi","hello","bye"]
l2 = ["shivam",'raj','roy']

for i in range(len(l1)):
    print(l1[i]+" "+l2[-(i+1)])
    # match first element of l1,
    # with last element of l2

#single line
res = [(l1[i],l2[-i-1]) for i in range(len(l1))]

print('Answer:')
print(res)