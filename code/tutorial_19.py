club = ['Jake', 'Anne', 'Bill']

is_member = 'Jake' in club
kick_out = 'Collin' not in club

print('Is Jake a member?', is_member)
print('Kickout Collin?', kick_out)

print('c' in 'scent')
print('ce' in 'scent')
print('cn' in 'scent')

jake_age = 15
anne_age = 15

# are these two variables pointing to the same memory address?
# this is not the same as == which compares the VALUES of the variables 
print( jake_age is anne_age)
