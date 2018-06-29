le =  input()
inp = input().split()
idx = int(input())
countofa = 0

import itertools
#print(inp,idx)
combinations = list(itertools.combinations(inp,idx))
ncom = len(combinations)

for eachcom in combinations:
    if 'a' in eachcom: 
        countofa +=1
#print(countofa,ncom)
l = list(filter(lambda x: 'a' in x, combinations)) #alternate code for the above for loop

if countofa:
    print(countofa/ncom)
else:
    print(countofa)
