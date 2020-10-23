# Required concepts: https://www.w3schools.com/python/python_intro.asp loops and strings

print('Question: Restore a string from its run length encoding, where each char, followed by its consecutive frequency')


string = 'a2b3c4'
res = '' 
# we want to encode as, val,consecutive fre
# aaabbbcccc is the desired output

for i in range(1,len(string),2):
  # visit only digits ;) on odd indices
  for _ in range(int(string[i])):
    res += string[i-1]
  # keep adding the prev character as many times as required


print('Answer:')
print(res)

print('Question: Restore a string from its run length encoding, where each char, followed by its consecutive frequency (may be ≥1 digit)')
# method if frequency is more than one digit!
string = 'a2b3c11'
res = '' 

freq = 0
cur_element = ''
for i in range(len(string)):
  # visit only digits ;) 
  if string[i].isdigit():
    freq = freq * 10 + int(string[i])
  else:
    res += cur_element * freq
    freq = 0
    cur_element = string[i]

res += cur_element * freq

print('Answer:')
print(res)