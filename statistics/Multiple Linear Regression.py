import numpy as np

m,n = input().split()
x_l,y_l = [],[]
for i in range(int(n)):
    *x1,y1 = map(float, input().split())
    x_l.append([1.]+x1)
    y_l.append(y1)

x= np.array(x_l)    #new x matrix
y= np.array(y_l)    # new y matrix
x_trans = np.transpose(x)       #transposing the x matrix
xx_trans = x_trans.dot(x)       #matrix multiplication with x and x^T
xx_trans_inv = np.linalg.inv(xx_trans)          #inversing the matrix(x.x^T)
xx_trans_invx_trans = xx_trans_inv.dot(x_trans) #matrix multiplication with (x.x^T).x^T
xx_trans_invx_transy = xx_trans_invx_trans.dot(y) # (x.x^T).x^T. Y
#print(xx_trans_invx_trans.shape,y.shape)
q = int(input())

for i in range(q):
    ft_set = list(map(float, input().split()))
    ft_set_array = np.array([1.]+ft_set)
    result = ft_set_array.dot(xx_trans_invx_transy)
    print(round(result,2))


#print(xx_trans_invx_transy)
