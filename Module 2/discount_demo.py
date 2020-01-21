quan=int(input("Enter the number of packages Purchased"))
if 20>quan>9:
    totalPrice=(99)*quan
    discount=(0.1*totalPrice) 
elif 50>quan>19:
    totalPrice=(99)*quan
    discount=(0.2*totalPrice) 
elif 100>quan>49:
    totalPrice=(99)*quan
    discount=(0.3*totalPrice)  
elif quan>100:
    totalPrice=(99)*quan
    discount=(0.4*totalPrice)
else:
    totalPrice=(99)*quan
    discount=0
print("discount = ",discount)
print("discounted price = ",totalPrice-discount)
