import numpy as np
inp = list(map(int, input().split()))

array = np.array(inp)
array.shape = (3,3) #inplace reshaping.
#new_array = np.reshaping(array,(3,3)) returns a new reshaped array
print(array)
