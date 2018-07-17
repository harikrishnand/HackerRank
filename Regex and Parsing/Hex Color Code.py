import re
no_of_lines = int(input())

for i in range(no_of_lines):
    inp = input()
    if not inp.startswith('#'):
        m = re.findall(r'(?<=#)[0-9A-Fa-f]{3,6}',inp)
        if m:
            print(*['#'+ str(n) for n in m], sep ='\n')
