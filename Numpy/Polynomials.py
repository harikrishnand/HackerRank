import numpy as np
coef = list(map(float,input().split()))

val = np.polyval(coef,int(input()))
print(val)
