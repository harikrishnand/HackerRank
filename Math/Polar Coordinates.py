Cno = complex(input())
import math
import cmath

r = math.sqrt(Cno.imag**2 + Cno.real**2)
print(r,cmath.phase(Cno), sep = '\n')
