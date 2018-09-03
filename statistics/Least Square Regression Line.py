x,y = [],[]
for i in range(5):
    p,q = input().split()
    x.append(int(p))
    y.append(int(q))

#y = a +bx
n = len(x)
x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)
xy = [xv*yv for xv,yv in zip(x,y)]
xi2 = [xv**2 for xv in x]
#print(xi2,x_mean,y_mean,xy)

# b = (n*sum(xy) - sum(x)*sum(y) )/ ( n*sum(x**2) - sum(x)**2)

b = ( ((n *sum(xy)) - sum(x)*sum(y)) /
     ( (n*sum(xi2)) - sum(x)**2)
    )
# a = y_mean - b*x_mean

a = y_mean - b*x_mean

stat_score = a + b * 80
print(round(stat_score,3))
