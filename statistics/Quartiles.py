#import numpy as np

def find_median(l):
    le = len(l)
    if le%2:
        median = l[le//2]
    else:
        median = (l[le//2] + l[(le//2)-1])/2
    return median

n = int(input())

inp = list(map(int,input().split()))
inp.sort()
#print(inp)
print(int(find_median(inp[:n//2])),
      int(find_median(inp)),
      int(find_median(inp[(n//2)+1 if n%2 else n//2:])),
      sep = '\n')
