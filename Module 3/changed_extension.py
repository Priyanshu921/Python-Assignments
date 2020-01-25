path=input("Enter the path")
path=path[::-1]
pathnew=path[path.index('.'):path.index('/')]
print(pathnew[::-1]+'pdf')

