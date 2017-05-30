
# basic
if True:
    print('I will run')

if False:
    print('I will not run')

# example
inventory = {'chairs':20, 'tables':5, 'drinks':103}
counted = sum(inventory.values())
actual = 130
is_invalid = False

if counted == actual:
    print('All items here.')
elif counted > actual:
    print('Extra items.')
elif counted < actual:
    if counted < 0:
        print('Invalid input. Cannot be negative.')
        is_invalid = True
    else:
        print('Missing items.')
else:
    print('Invalid input.')
    is_invalid = True


if not is_invalid:
    print('Inventory check complete.')
else:
    print('Recount required.')
