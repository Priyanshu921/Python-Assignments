k = 0
for i in range(1,7) :     
    for j in range(i,7) : 
        print(' ', end='') 
    while (k != (2 * i - 1)) : 
        if (k == 0 or k == 2 * i - 2) : 
            print('*', end='') 
        else :
            print(' ', end ='') 
        k = k + 1
    k = 0; 
    print ("") 
for i in range(0, 13) : 
    print ('*', end = '') 
