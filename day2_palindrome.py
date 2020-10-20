# Required concepts:  list slicing https://www.w3schools.com/python/ref_func_slice.asp

print('Question: check if a string is a palindrome')

word1 = "hello"
word2 = "level"
#now I want the reverse word
reverse_word1 = word1[::-1]
reverse_word2 = word2[::-1]
#i got the reverse by slicing with a step of -1, so basically from the last element upto the first, negative step value means right to left 
#like for(int i = n ; i>=0 ; i--)

print('Answer:')
print(word1,' is ',word1 == reverse_word1)
print(word2,' is ',word2 == reverse_word2)
#If you are same as your reverse, you are a palindrome
