no_of_shoes = int(input())
all_shoes = map(int, input().split())
no_of_customer = int(input())
money_earned  = 0

from collections import Counter
shoes_shelve = Counter(all_shoes)

#print(shoes_shelve)
for i in range(no_of_customer):
    size,price = map(int,input().split())
    if shoes_shelve[size] > 0:
        money_earned +=price
        shoes_shelve[size] -= 1
    
print(money_earned)
