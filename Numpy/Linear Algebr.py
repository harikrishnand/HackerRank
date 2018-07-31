import numpy as np
np.set_printoptions(legacy= '1.13')
array_inp = [input().split() for i in range(int(input()))]
array = np.array(array_inp,float)
print(np.linalg.det(array))
