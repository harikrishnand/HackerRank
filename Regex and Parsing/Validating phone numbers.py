import re
no_of_inputs = int(input())

for i in range(no_of_inputs):
    inp = input()
    m = re.match(r'[789]{1}[0-9]{9}$',inp)
    if m:
        #print(m.group())
        print('YES')
    else:
        print('NO')
