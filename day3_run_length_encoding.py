# Required concepts: https://www.w3schools.com/python/python_intro.asp loops and strings

print('Question: Convert a string into its run length encoding, each char, followed by its consecutive frequency')

string = 'aaabbbcccc'
res = '' 
# we want to encode as, val,consecutive fre
# a3b3c4 is the desired output

cur_freq = 0
for i in range(len(string)-1):
  if string[i] == string[i+1]:
    cur_freq += 1
  else:
    res += string[i] + str(cur_freq)
    cur_freq = 1
res += string[-1] + str(cur_freq)

print('Answer:')
print(res)

"""
alternate easy method:
cur_freq = 0
cur_element = string[0]

for element in string:
  if element == cur_element:
    cur_freq +=1 
  else:
    res += cur_element + str(cur_freq)
    cur_freq = 1
    cur_element = element

res += cur_element + str(cur_freq)
"""