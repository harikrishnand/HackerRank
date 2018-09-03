n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

pos = lambda val,l: sorted(l).index(val)+1

rx = [pos(val,x) for val in x]
ry = [pos(val,y) for val in y]

di = [(xv - yv) for xv,yv in zip(rx,ry)]
di2 = sum(map(lambda x: x**2, di))
#print(di2)

rxy = 1-((6*di2)/
         ((n**3)-n)
        )
print(round(rxy,3))
