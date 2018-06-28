A = list(map(int,input().split()))
B = list(map(int,input().split()))

import itertools

print(*list(itertools.product(A,B)), sep=' ') #another way to print the list
