no_of_tries = int(input())

for i in range(no_of_tries):
    try:
        a,b = input().split()
        print(int(int(a)/int(b)))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:',e)
