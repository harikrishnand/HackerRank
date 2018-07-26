import numpy as np

array = np.array([v for v in input().split()],dtype=float)
np.set_printoptions(sign= ' ')
print(np.floor(array),np.ceil(array),np.rint(array),sep = '\n')
