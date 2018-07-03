no_of_cmds = int(input())
from collections import deque
d = deque()

for i in range(no_of_cmds):
    cmd,*inp = input().split()
    #print(cmd,inp)
    if inp:
        getattr(d,cmd)(int(inp[0]))
    else:
        getattr(d,cmd)()
print(*d,sep=' ')

#----------------------Alterantive------------------------------------------#

no_of_cmds = int(input())
from collections import deque
d = deque()

for i in range(no_of_cmds):
    cmd,*inp = input().split()
    #print(cmd,*inp)
    getattr(d,cmd)(*inp)    #* is 0 or more
print(*d,sep=' ')
