import email.utils,re
no_of_input = int(input())

for i in range(no_of_input):
    inp = input()
    name,mailid= email.utils.parseaddr(inp)
    validemail = re.match(r'[^_0-9.-][\w.-]*@{1}([^_0-9.-])+\.{1}([^_0-9.-]){1,3}$',mailid)
    #validemail = re.match(r'[a-zA-Z](\w¦\.¦-)+@[a-zA-Z]+\.[a-zA-Z]{1,3}',mailid)
    if validemail:
        print(validemail.groups())
        print(inp)
    #print(mailid)
