FO,TO = map(int, input().split())
n = int(input())

def Geo_Distribution(n,p,q):
    GD = (q**(n-1))*p
    return GD
p = FO/TO
q = 1-p
Tot_GD = 0.0
for i in range(1,n+1):
    Tot_GD += Geo_Distribution(i,p,q)
    #print(Tot_GD)

print('{:.03f}'.format(Tot_GD))
