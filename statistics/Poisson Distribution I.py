import math

def poisson_Dis(m,k):
    PD = ((m**k)*(2.71828**(-m)))/math.factorial(k)
    return PD

m = float(input())
k = int(input())

print('{:.03f}'.format(poisson_Dis(m,k)))
