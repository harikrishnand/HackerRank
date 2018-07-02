As,Bs = map(int,input().split())
from collections import defaultdict

Aset = defaultdict(list)

for i in range(As):
    Aset[input()].append(i+1)
    
#print(Aset)

for j in range(Bs):
    inp = input()
    if inp in Aset:
        print(*Aset[inp])
    else:
        print(-1)
