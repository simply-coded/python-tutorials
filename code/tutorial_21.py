# basic
if True:
    print('i will run')

if False:
    print('i will not run')    

# video example
inventory = {'chairs': 20, 'tables': 5, 'drinks': 103}
actual = 130
counted = sum(inventory.values())
is_invalid = False

if counted == actual:
    print('all items here')
elif counted > actual:
    print('extra items')
elif counted < actual:
    if counted < 0:
        print('negative input. please check again')
        is_invalid = True
    else:
        print('missing items')
else:
    print('invalid input. please check again')
    is_invalid = True


if not is_invalid:
    print('inventory check complete')
