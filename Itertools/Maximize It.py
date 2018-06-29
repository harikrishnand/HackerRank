nlist,modno = map(int,input().split())
alllist = []
import itertools
for i in range(nlist):
    a,*b = map(int,input().split())
    alllist.append(list(b))
  
allcombination = list(itertools.product(*alllist))

#print(alllist,allcombination) 
    
allres = list(map(lambda x: sum(i**2for i in x)%modno, allcombination))           
print(max(allres))
