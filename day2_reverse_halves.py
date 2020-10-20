# Required concepts: https://www.w3schools.com/python/python_intro.asp Everything till for loops

print('Question: return reverse first half of l1 and reverse of second half of l2')

l1 = ['a' , 'b' , 'c' , 'd']
l2 = ['e' , 'f' , 'g' , 'h']

# reverse first half of l1 and second of l2
# we want: ['b' , 'a' , 'h' , 'g']

# cut the first list into first half reverse and second into second half reverse
half1 = len(l1)//2 - 1
half2 = len(l2)//2 - 1
# -1 for 0 based indicing
result =  l1[half1::-1] + l2[:half2:-1]

print('Answer:')
print(result)

