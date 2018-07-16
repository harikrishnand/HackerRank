import re
inp = input()
mat = input()

m = re.compile(r""+ re.escape(mat) +r"")
st = 0
for i in  range(len(inp)):
    reobj =  m.search(inp,st)
    if reobj:
        print((reobj.start(),reobj.end()-1))
        if len(mat) == 1:
            st = reobj.end()
        else:
            st = reobj.end()-1
    else:
        break
if not st:
    print('(-1, -1)') 
