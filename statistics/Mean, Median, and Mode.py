import numpy as np
from collections import Counter

no_of_inp = int(input())
array = np.array(list(map(int , input().split())))
mode_val = Counter(array)
mode = sorted(mode_val.items(),key = lambda x: (-x[1],x[0]))

print('{:.1f}'.format(np.mean(array)),'{:.1f}'.format(np.median(array)),mode[0][0],sep = '\n')
