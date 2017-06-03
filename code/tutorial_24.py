
# basic syntax
'''
while True:
    print('will loop forever')

while False:
    print('will never loop')

init = True
while your_condition or init:
    init = False
    print('will loop at least once')
'''

# video example
num = ''

# loop until user enters a digit
init = True
while not num.isdigit() or init:
    init = False
    num = input('Check for prime of: ')

# convert string digit to integer
num = int(num)

# basic prime check and setup
if num <= 1:
    print(num, 'is not prime.')
    check_more = False
else:
    divisor = num - 1
    check_more = True

# more indepth check (examples of break and continue)
while check_more:
    if divisor == 1:
        print(num, 'is prime.')
        break

    if (num % divisor) == 0:
        print(num, 'is not prime.')
        check_more = False
        continue 

    divisor -= 1
