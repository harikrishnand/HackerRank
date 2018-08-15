import math
m,sd = map(int, input().split())

Cu_Pro = lambda x: .5 *(1 + math.erf( (x-m)/(sd*math.sqrt(2)) ))

score_higher = int(input())
pass_score = int(input())
#print(score_higher,pass_score)
print(round((1-Cu_Pro(score_higher))*100,2))
print(round((1-Cu_Pro(pass_score))*100,2))
print(round((Cu_Pro(pass_score))*100,2))
