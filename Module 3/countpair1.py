from itertools import *
n=int(input("Enter the number of elements"))
sum1=int(input("Enter the sum"))
x=list(map(int,input().strip().split()))[:n]
list1=list(combinations(x,2))
for x in list1:
        if sum(x)==sum1:
            print(x)
