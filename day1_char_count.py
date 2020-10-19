# Required concepts: https://www.w3schools.com/python/python_intro.asp Everything till for loops

countOfChar = {
 #store the count of all chars
 #as a pair
 #eg. 'a' : 5
 #    'b' : 6
}

string = "hello rashil"

for char in string:
  if char in countOfChar:
    countOfChar[char]+=1
    #he has already been found just increment him
  else:
    countOfChar[char] = 1
    #he was not found so i initilized him

print(countOfChar)