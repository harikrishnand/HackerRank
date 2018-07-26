import numpy as np
r,c = input().split()

array_inp = [[int(v) for v in input().split()] for i in range(int(r))]
array = np.array(array_inp)
min_array = np.min(array,axis=1)
max_array = np.max(min_array)

print(max_array)
