
# ternary operator syntax
# result = A if condition else B

# basic
print('Yes' if True else 'No')
print('Yes' if False else 'No')

# example 1
person_age = 17
allowed_in = 'Yes' if person_age >= 18 else 'No' 

print('Should I allow them in?', allowed_in)

# example 2
item_a = 38.21
item_b = 34.58

cheapest = item_b if item_b < item_a else item_a

# if statement equivalent
if item_b < item_a:
    cheapest = item_b
else:
    cheapest = item_a

print(f'The cheapest price is ${cheapest}')


# example 3
item_a = {'name':'Item A', 'price':38.21, 'quality':'new'}
item_b = {'name':'Item B', 'price':34.58, 'quality':'used'}

# nested if (decent)
if item_a['price'] > item_b['price']:
    if (item_a['quality'] == 'new') and (item_b['quality'] == 'used') and (item_a['price'] - item_b['price'] <= 5):
        best = item_a
    else:
        best = item_b
else:
    if (item_a['quality'] == 'used') and (item_b['quality'] == 'new') and (item_b['price'] - item_a['price'] <= 5):
        best = item_b
    else:
        best = item_a

# if with ternary (clutter face)
if item_a['price'] > item_b['price']:
    best = item_a if (item_a['quality'] == 'new' and item_b['quality'] == 'used' and item_a['price'] - item_b['price'] <= 5) else item_b

else:
    best = item_b if (item_a['quality'] == 'used' and item_b['quality'] == 'new' and item_b['price'] - item_a['price'] <= 5) else item_a
 

# just ternary (nightmare fuel)
best = (item_a if (item_a['quality'] == 'new' and item_b['quality'] == 'used' and item_a['price'] - item_b['price'] <= 5) else item_b) if (item_a['price'] > item_b['price']) else (item_b if (item_a['quality'] == 'used' and item_b['quality'] == 'new' and item_b['price'] - item_a['price'] <= 5) else item_a)

print('The best item is', best['name'])
