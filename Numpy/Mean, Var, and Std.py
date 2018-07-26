import numpy as np

r,c = input().split()

array_inp = [[int(v) for v in input().split()] for i in range(int(r))]
array = np.array(array_inp)
np.set_printoptions(legacy= '1.13')
print(np.mean(array,axis=1),np.var(array,axis=0), np.std(array),sep='\n')
