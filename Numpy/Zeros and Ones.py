import numpy as np
inp =  tuple(map(int, input().split()))

print(np.zeros(inp,dtype = int),np.ones(inp, dtype = int),sep = '\n')
