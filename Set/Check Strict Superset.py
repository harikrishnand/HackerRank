Super_Set = set(input().split())
nset = int(input())
isSuper = 'True'
#print(Super_Set)
for i in range(nset):
    tset = set(input().split())
    #print(tset)
    if not Super_Set.issuperset(tset):
        isSuper = 'False'
print(isSuper)
