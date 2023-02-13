from collections import OrderedDict

n = int(input())
name = []
price = []
for i in range(n):
    item = input().split()
    name.append(" ".join(item[:-1]))
    price.append(item[-1])

item_dict = OrderedDict()

for (item_name,pr) in zip(name,price):
    item_price = int(pr)
    if item_name in item_dict:
        item_dict[item_name] += item_price
    else:
        item_dict[item_name] = item_price

for item, price in item_dict.items():
    print(item, price)
