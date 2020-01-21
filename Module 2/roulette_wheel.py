pocketNo=int(input("Enter the Pocket Number"))
if pocketNo==0:
    print("The Color of the Pocket is green")
elif 10>=pocketNo>0 or 28>=pocketNo>18:
    if pocketNo%2==0:
        print("The Color of the Pocket is black")
    else:
        print("The Color of the Pocket is red")
elif 18>=pocketNo>10 or 36>=pocketNo>28:
    if pocketNo%2==0:
        print("The Color of the Pocket is red")
    else:
        print("The Color of the Pocket is black")
else:
    print("Pocket Number Should be Between 0 and 36")
