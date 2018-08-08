#import numpy
n =int(input())
array = map(int, input().split())
weight = list(map(int, input().split()))

mul = map(lambda x: x[0]*x[1],zip(array,weight))
print('{:.1f}'.format(sum(mul)/sum(weight)))
