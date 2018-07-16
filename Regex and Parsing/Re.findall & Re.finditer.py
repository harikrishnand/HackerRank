import re

n = re.findall(r'([^AEIOUaeiou])?([AEIOUaeiou]{2,})([^AEIOUaeiou]{1})',input())
#re.findall(r'([^AEIOUaeiou])*([AEIOUaeiou]{2,})([^AEIOUaeiou])+',input())
if n:
    #print(n)
    print(*[v[1] for v in n],sep='\n')
else:
    print('-1')
