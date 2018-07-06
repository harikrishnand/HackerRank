no_std,no_sub = map(int, input().split())
marksheet = []

for i in range(no_sub):
    sub = tuple(map(float, input().split()))
    marksheet.append(sub)    
print(*[sum(std)/no_sub for std in zip(*marksheet)],sep = '\n')
