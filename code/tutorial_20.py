# and combos
print('True and True =', True and True )
print('True and False =', True and False )
print('False and True =', False and True )
print('False and False =', False and False )

# or combos
print('True or True =', True or True )
print('True or False =', True or False )
print('False or True =', False or True )
print('False or False =', False or False )

# not combos
print('not True =', not True )
print('not False =', not False)
print('not (True or False) =', not (True or False))

# video example
ticket_buyers = ['Jake', 'Alice', 'Bill']
buyer = 'Alice'
buyer_age = 12
has_adult = True

let_in = (buyer in ticket_buyers) and (buyer_age >= 18 or has_adult)

print('Should I let them in?', let_in)
