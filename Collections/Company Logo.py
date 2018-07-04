#!/bin/python3

import math
import os
import random
import re
import sys
def findlogo(s):
    
    from collections import Counter
    #from collections import defaultdict
    #from collections import OrderedDict
    #from itertools import groupby
    Ord_logo = OrderedDict()
    logo = Counter(s)
    #print(logo.items())
    sor_logo = sorted(logo.items(),key = lambda x: (-x[1],x[0]))[:3]
    #print(sor_logo)
    print(*[k+ ' ' + str(v) for k,v in sor_logo], sep='\n')
    
    
    
    
"""    #logo1 = sorted(logo)[:3]
    #lis = [(k,list(ls)) for k,ls in groupby(logo,key= lambda x:x[1])]
    print(logo)
    
    sort_logo = defaultdict(list)
    for k,v in (sorted(logo,key= lambda x: x[1],reverse = True)):
        sort_logo[v].append(k)
        Ord_logo[v]= sort_logo[v]
    print(sort_logo,Ord_logo)
    for k,ls in Ord_logo.items():
        for v in range(3):
            print(sorted(ls)[v],k,sep=' ')
"""

if __name__ == '__main__':
    s = input()
    findlogo(s)
