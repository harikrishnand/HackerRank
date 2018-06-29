nlist,modno = map(int,input().split())
allnumbers = []
alllist = []
import itertools
for i in range(nlist):
    a,*b = map(int,input().split())
    alllist.append(list(b))
    allnumbers += list(b)
allcombination = list(itertools.combinations(allnumbers,nlist))

#print(alllist,allnumbers,allcombination) 

def calcpow(*a): 
    """ Function will check is it a valid a combination. If yes then it will calculate the modno        for the combination and reurnt the mod value."""
    res = 0
    for i in range(len(a)):
        if a[i] not in alllist[i]:
            break
    else:
        res = sum(list(map(lambda x: x**2,a)))%modno
    return res
        
    
allres = list(itertools.starmap(calcpow, allcombination))           
print(max(allres))
