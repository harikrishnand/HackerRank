import numpy as np
n,m,p = input().split()

inp_n =[[int(v) for v in input().split()] for i in range(int(n))]
inp_m =[[int(v) for v in input().split()] for i in range(int(m))]

array_n = np.array(inp_n)
array_m = np.array(inp_m)

print(np.concatenate((array_n,array_m),axis = 0)) # to concatenate in axis 0(row), axis 1 must be same(column) between both arraies and vice versa
