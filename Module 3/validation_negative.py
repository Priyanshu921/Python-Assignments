wholeSaleValue=0.0
while(True):
    wholeSale=float(input("Enter the Wholesale Price"))
    if wholeSale<0:
        continue
    else:
        wholeSaleValue+=wholeSale
    ch=input("press Y to continue and N to exit")
    if(ch=='n' or ch=='N'):
        break
print("Retail Price = ",wholeSaleValue*0.5)
