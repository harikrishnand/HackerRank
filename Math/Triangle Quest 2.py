for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print([0,1,121,12321,1234321,123454321,12345654321,1234567654321,123456787654321,12345678987654321][i])   
    print((10**i//9)**2) #alternate solution.
    
    #print (*(range(1,i+1))[:-1], *(range(1,i+1))[::-1], sep='' )
