no_of_items = int(input())
from collections import OrderedDict
from collections import defaultdict
price_of_item = defaultdict(int)
item_pursesed = OrderedDict()
for i in range(no_of_items):
    *item,price = input().split()
    price_of_item[' '.join(item)] += int(price)
    item_pursesed[' '.join(item)] = price_of_item[' '.join(item)]
    
#print('{0} {1}'.format(*list(item_pursesed.items())), sep = '\n')

for k,v in item_pursesed.items():
    print(k,v)
#D[item] = D.get(item, 0) + int(price) can be used to get the value of a key, If not present then default tpo 0
