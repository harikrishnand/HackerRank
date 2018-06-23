nInp = int(input().split()[0])
Mainlist = list(map(int, input().split()))
HappySet = set(map(int,input().split()))
SadSet = set(map(int,input().split()))
Happy = 0
Sad = 0
#print(HappySet,SadSet)

for l in Mainlist:
    if l in HappySet:
        Happy +=1
        #print(l)
    elif l in SadSet:
        Sad +=1
        #print(l)
    else: pass
print(Happy-Sad)
