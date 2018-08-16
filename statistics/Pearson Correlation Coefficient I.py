import math

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

mx = sum(x)/len(x)
my = sum(y)/len(y)

sdx = math.sqrt(sum([(xv-mx)**2 for xv in x])/len(x))
sdy = math.sqrt(sum([(yv-my)**2 for yv in y])/len(y))

correlation_cof = sum([(a-mx)*(b-my) for a,b in zip(x,y)])/(n*sdx*sdy)

print(round(correlation_cof,3))

#print(mx,my,sdx,sdy)
