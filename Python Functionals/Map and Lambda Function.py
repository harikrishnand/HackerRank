cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):           # return a list of fibonacci numbers
    res = [0,1]
    while len(res)<= n:
        res.append(sum(res[-2:]))
    return(res[:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


###########Alternative code for Fab. #########

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b
