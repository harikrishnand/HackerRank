
import re
no_of_lines = int(input())

def change(v):
    #print(v.group())
    #print(v.start(),v.end())
    if v.group() == '&&' and l[int(v.start())-1] == ' ' and l[int(v.end())] == ' ':
        return 'and'
    elif v.group() == '||' and l[int(v.start())-1] == ' ' and l[int(v.end())] == ' ':
        return 'or'
    else: 
        return v.group()
        
 
for i in range(no_of_lines):
    l = input()
    l = re.sub(r'[&]{2}',change,l)
    #print(l)
    print(re.sub(r'[|]{2}',change,l))
    
#print(no_of_lines)





################################Alternate solution #########################

import re
N = int(raw_input())

for i in range(N):
    print re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', raw_input())
