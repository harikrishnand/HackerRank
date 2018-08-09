#import numpy
import math

n = int(input())
inp = list(map(int,input().split()))

mean = sum(inp)/len(inp)
variance = sum([(x-mean)**2 for x in inp])/len(inp)
std_Deviation = math.sqrt(variance)
print('{:.1f}'.format(std_Deviation))
