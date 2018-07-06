x, res = map(int,input().split())
equation = input()
equation = equation.replace('x',str(x))
if res == eval(equation):
    print(True)
else:
    print(False)
print(x,res,equation,res,exec(equation),eval(equation))
