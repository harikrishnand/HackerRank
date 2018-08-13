import math as m


def comb(n,x):
    return m.factorial(n)/(m.factorial(x)*m.factorial(n-x))

def binomial_dist(n,x,p,q):
    c = comb(n,x)
    val = c*(p**x)*(q**(n-x))
    #print(c,val,p**x,q**(n-x))
    return val

pb,pg = map(float, input().split())
p = pb/(pb+pg)
q = 1-p
bd = 0.0
#print(p,q)
for i in range(3,7):
    bd += binomial_dist(6,i,p,q)
 
print('{:.03f}'.format(bd))
