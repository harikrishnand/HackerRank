
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int('1'*i)*i) 
    
    print((10**i//9)*i) #without using the string literal.


#print(int('1'*i)*i) alternate solution but invalid as it uses string literl 
