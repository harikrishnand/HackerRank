no_of_testcases = int(input())

for i in range(no_of_testcases):
    nA = int(input())
    A = set(map(int, input().split()))
    nB = int(input())
    B = set(map(int,input().split()))
    #print(A,B)
    if A.issubset(B):
        print('True')
    else:
        print('False')
