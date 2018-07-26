import numpy as np
r,c = input().split()

inp_a = [[int(v) for v in input().split()] for i in range(int(r))]
inp_b = [[int(v) for v in input().split()] for i in range(int(r))]

A = np.array(inp_a)
B = np.array(inp_b)
np.set_printoptions(formatter = {'float_kind': lambda x: "%d" % x}) #'{0:d}'.format})
print(A+B,A-B,A*B,A/B,A%B,A**B,sep='\n')
