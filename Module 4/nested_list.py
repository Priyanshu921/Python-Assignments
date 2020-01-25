matrix=[]
for i in range(5):
    matrix.append([])#appending an empty list
    for j in range(5):
        matrix[i].append([j+i])
print(matrix)
matrix=[[j for j in range(5)]for i in range(5)]#matrix Comprehension
print(matrix)

matrix=[[1,2,3],[4,5,6],[7,8,9]]#to flatten a 2d matrix i,e,. to convert it in 1D Matrix
flatten_matrix=[]
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)
flatten_matrix=[val for sublist in matrix for val in sublist]#second way to flatten a 2D matrix
print(flatten_matrix)

planets=[['Mercury','Venus','Jupiter'],['Mars','Earth','Saturn'],['Uranus','Neptune','Pluto']]
flatten_planets=[planet for sublist in planets for planet in sublist if len(planet)<6]#flatten 2d list with length condition
print(flatten_planets)
