m=float(input())
n=int(input())
profit=0
x=list(map(int,input().strip().split()))[:n]
while m>=0:
    ind=x.index(max(x))
    profit+=max(x)
    m-=0.5
    x[ind]=-1
    ind2=x.index(max(x))
    m-=(abs(ind-ind2)*0.5)
print(profit)
