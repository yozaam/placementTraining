# Required concepts: https://www.w3schools.com/python/python_intro.asp lists and functions

print('Question: Element which is min in row and max in column')
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def rowMinColMax(matrix):
  rowMin,colMax = [],[]
  for row in matrix:
    rowMin.append(min(row))
  for i in range(len(matrix[0])):
    maxi = matrix[0][i]
    for j in range(len(matrix)):
      maxi = max(maxi,matrix[j][i])
    colMax.append(maxi)

  #now find the overlap
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if rowMin[i] == colMax[j] == matrix[i][j]:
        return matrix[i][j]
  return False

print('Answer:')
print(rowMinColMax(matrix))





