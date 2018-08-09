#import numpy
from itertools import repeat

def find_median(l):
    le = len(l)
    return l[le//2] if le%2 else (l[le//2] + l[(le//2)-1])/2

n = int(input())
inp_raw = zip(map(int, input().split()),map(int, input().split()))
inp = []

for x in inp_raw:
    inp += list(repeat(*x)) 

    inp.sort()
#print(inp)
q1 = find_median(inp[:len(inp)//2])
q3 = find_median(inp[(len(inp)//2)+1 if len(inp)%2 else len(inp)//2:])

print('{:.1f}'.format(q3-q1))
