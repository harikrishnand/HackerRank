input_str = input()

ls=us=on=en= ''

for c in input_str:
    if c.isdigit():
        if not int(c)%2:
            en += c
        else:
            on += c
    else:
        if c.islower():
            ls += c
        else:
            us += c
print(*(sorted(ls) + sorted(us) + sorted(on) + sorted(en)), sep='')

# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
