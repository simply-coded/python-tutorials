from getpass import getpass

# example 1
name = input('enter your name: ')

if name == '':
    print('dont leave field blank. run again')
elif not name.isalpha():
    print('only letters allowed. run again')
else:
    print('welcome,', name)


# example 2
username = input('enter in your username: ')
password = getpass('enter in your password: ')

print(username, password)


# example 3
a = input('first number : ')
b = input('second number: ')

if a.replace('.','',1).isdigit() and b.replace('.','',1).isdigit():
    a = float(a)
    b = float(b)
    print('result is =', a + b)
else:
    print('only numbers allowed. run again')
