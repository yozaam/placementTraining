countOfChar = {


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