import re
no_of_inputs = int(input())

for n in range(no_of_inputs):
    print(bool(re.match(r'[-+]{,1}[0-9]*\.[0-9]{1,}$',input())))
    #if nm:
    #    print(nm.group())
    #print(nm)
