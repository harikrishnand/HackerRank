import numpy as np
r,c = input().split()

arr = np.eye(int(r),int(c), k =0)
np.set_printoptions(sign=' ')
print(arr)
