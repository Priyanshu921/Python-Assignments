stR=str(input("Enter the String containg marks").split('=')).split(' ')
sum=count=0
for x in stR:
    if x.isdigit():
        sum+=int(x)
        count+=1
print('sum=',sum,'\npercentage',sum/count)
