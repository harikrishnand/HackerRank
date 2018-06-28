inp,r = input().split()

import itertools
for res in sorted(list(itertools.permutations(inp,int(r)))):
    print(''.join(res), sep = '\n')
#print(''.join(), sep = '\n')
#print(*res[0], sep='\n')   #doesn't works.

# alternate is to sort the input strin before passing to the itertools.
