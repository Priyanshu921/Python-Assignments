from itertools import *
def countPairs(list3):
    for x in list3:
        if sum(x)==sum1:
            print(x)
n=int(input("Enter the number of elements"))
sum1=int(input("Enter the sum"))
x=list(map(int,input().strip().split()))[:n]
y=list(map(int,input().strip().split()))[:n]
list1=list(combinations(x,2))
list2=list(combinations(y,2))
countPairs(list1)
countPairs(list2)

