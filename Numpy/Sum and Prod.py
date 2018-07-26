import numpy as np
r,c = input().split()

array_inp = [[int(v) for v in input().split()] for i in range(int(r))]
array = np.array(array_inp)
array_sum = np.sum(array,axis=0)
array_prd = np.prod(array_sum)
print(array_prd)
