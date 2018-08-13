import math as m


def comb(n,x):
    return m.factorial(n)/(m.factorial(x)*m.factorial(n-x))

def binomial_dist(n,x,p,q):
    c = comb(n,x)
    val = c*(p**x)*(q**(n-x))
    #print(c,val,p**x,q**(n-x))
    return val

p_per,n = map(int, input().split())
p = p_per/100
q = 1-p
BD1 = 0.0
#print(p,q)
for i in range(3):
    BD1 += binomial_dist(n,i,p,q)
print('{:.03f}'.format(BD1))
BD2 = 0.0
for i in range(2,n+1):
    BD2 += binomial_dist(n,i,p,q)
print('{:.03f}'.format(BD2))
