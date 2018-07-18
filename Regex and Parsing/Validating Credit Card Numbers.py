import re

val1 = re.compile(r'^[456]+[0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}$')
val2 = re.compile(r'.*(.)\1{3}.*')

for i in range(int(input())):
    inp = input()
    m1 = val1.match(inp)
    m2 = val2.match(inp.replace('-',''))
    #if m2:
    #    print('m2:' + m2.group())
    if m1 and not m2:
        print('Valid')
    else:
        print('Invalid')
