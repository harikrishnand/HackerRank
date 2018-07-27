import numpy as np
r = int(input())

ar1 = [input().split() for i in range(r)]
ar2 = [input().split() for i in range(r)]
array1 = np.array(ar1,int)
array2 = np.array(ar2,int)
#print(array1,array2)
print(array1.dot(array2))
