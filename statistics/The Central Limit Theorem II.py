import math
x= int(input())
n = int(input())
m = float(input())*n
sd = float(input())*math.sqrt(n)

Cu_Pro = lambda x: .5 *(1 + math.erf( (x-m)/(sd*math.sqrt(2)) ))

print(round(Cu_Pro(x),4))
