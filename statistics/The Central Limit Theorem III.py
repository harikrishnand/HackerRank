import math

n = int(input())
m = int(input())
true_std_dev = int(input())
per = float(input())
z = float(input())

sample_std_dev = true_std_dev/math.sqrt(n)

find_interval = lambda z: z*sample_std_dev + m

print('{:.02f}'.format(find_interval(-z)))
print('{:.02f}'.format(find_interval(z)))
