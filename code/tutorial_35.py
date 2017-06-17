import random

# restaurant menu
menu = {
    'Hamburger':4.00,
    'Cheeseburger':4.50,
    'Bacon Cheeseburger':5.00,
    'Hot Dog':2.50,
    'Chili Dog':4.50,
    'Pulled Pork Sandwich':5.00,
    'Grilled Chicken Sandwich':4.50,
    'Philly Cheese Steak':6.50,
    'Deli Turkey Sandwich':6.00,
    'Wrap Sandwich':6.00,
    'Chicken Strips':6.50,
    'Bowl of Soup':6.00,
    'Salad':6.50,
    'Fries':2.00,
    'Onion Rings':3.50,
    'Cheese Sticks':5.00,
    'Chips':1.50    
}

# video challenge
def get_money(customer, amount):    
    # calculate money needed to cover the "amount" to the nearest 5 dollar bill
    
    # take that money out of the customers wallet

    # return the money you calculated to pay for the meal

    return 100

# receipt function
def receipt(customer):
    order_summary = ''
    order_total = 0
    for item, price in customer['ordered']:
        order_summary += f'{item} {price}\n'
        order_total += price

    payed_with = get_money(customer, order_total)
    change_due = payed_with - order_total

    return '\n'.join([
        f'=============================', 
        f'Thank you for dinning with',
        f'us {customer["name"]}.',
        f'-----------------------------',
        f'{order_summary[:-1]}',
        f'-----------------------------',
        f'Total is ${order_total}',
        f'Payed with ${payed_with}',
        f'Change Due ${change_due}',
        f'============================='
    ])

menu_items = list(menu.items())
    
# create the customers
cust1 = {
    'name': 'Alice Miller',
    'wallet': 103.57,
    'ordered': random.sample(menu_items, random.randint(1,8))
}

cust2 = {
    'name': 'Mark Penton',
    'wallet': 82.45,
    'ordered': random.sample(menu_items, random.randint(1,8))
}

# print out their receipts
print(receipt(cust1), receipt(cust2), sep='\n')
