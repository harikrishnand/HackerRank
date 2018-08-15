import math

def Cumulative_Probability(m,sd,x):
    ND = 0.5*(1+ math.erf((x-m)/(sd*(math.sqrt(2)))))
    return ND
    
m,sd = map(int, input().split())
x = float(input())
y,z = map(float, input().split())
#print(m,sd,x)
print('{:.03f}'.format(Cumulative_Probability(m,sd,x)))
print('{:.03f}'.format(Cumulative_Probability(m,sd,z) - Cumulative_Probability(m,sd,y)))
