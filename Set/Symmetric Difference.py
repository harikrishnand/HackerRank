Nn = input()
N = input()
Mn = input()
M = input()
difset = set()
nset = set((map(int,N.split())))
mset = set((map(int,M.split())))
#print(nset,mset)

#difset.update(nset.difference(mset))
#difset.update(mset.difference(nset))

difset.update(nset^mset)
    
print('\n'.join(map(str,sorted(difset))))
