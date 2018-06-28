inp, r = input().split()

import itertools

for i in range(1,int(r)+1):
    print(*[''.join(x) for x in itertools.combinations(sorted(inp),i)], sep='\n')    # returns all the unique combinaions not permuatations. Ex only returns HK not HH or KH
    #print([''.join(x) for x in itertools.combinations_with_replacement(sorted(inp),i)], sep='\n')  returns only the unique combination including repeatation ex: HH,CC,HK but not KH
    
    #print([''.join(x) for x in itertools.permutations(sorted(inp),i)], sep='\n') returns all the possibilities ex: AC,CA,HK,KH but not HH or CC
