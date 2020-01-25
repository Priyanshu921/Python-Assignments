string=input().split(' ')
string1=set(string)
string2=(list(string1))
string2.sort()
for i in string2:
    print(i,end=" ")
