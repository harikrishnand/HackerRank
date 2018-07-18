import re

exp1 = re.compile(r'[a-zA-Z0-9]{10}')
exp2 = re.compile(r'.*[A-Z]+.*[A-Z]+.*$')
exp3 = re.compile(r'.*[0-9]+.*[0-9]+.*[0-9].*$')
exp4 = re.compile(r'^(?:([A-Za-z0-9])(?!.*\1))*$')
for i in range(int(input())):
    inp = input()
    m = exp1.match(inp)
    m2 = exp2.match(inp)
    m3 = exp3.match(inp)
    m4 = exp4.match(inp)
    if m and m2 and m3 and m4:
        #print(m.group(),m2.group(),m3.group(),m4.group())
        print('Valid')
    else:
        print('Invalid')
        
        
        
        
################################Alternative#######################################

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
