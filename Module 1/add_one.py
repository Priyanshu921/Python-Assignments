x=input("Enter any Five Digit Number")
sum=[1,1,1,1,1]
for i in range(len(x)):
    sum[i]=sum[i]+int(x[i])
print("".join(map(str,sum)))
