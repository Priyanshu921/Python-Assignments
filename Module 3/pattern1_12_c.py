for k in range(4):
    for j in range(4):
        print(" "*(6-j-k),end="")
    print("*   "*(2*k+1))
for k in range(2,-2,-1):
    for j in range(4):
        print(" "*(6-j-k),end="")
    print("*   "*(2*k+1))
