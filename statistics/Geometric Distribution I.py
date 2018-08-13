FO,TO = map(int, input().split())
n = int(input())

def Geo_Distribution(n,p,q):
    GD = (q**(n-1))*p
    return GD
p = FO/TO
q = p-1

print('{:.03f}'.format(Geo_Distribution(n,p,q)))
