### Recap
name = 'John'

a = 'My name is ' + name + '!'
b = f'My name is {name}!'
c = 'My name is {}!'.format(name)
d = 'My name is {0}!'.format(name)
e = 'My name is {f_name}!'.format(f_name=name)
f = 'My name is %s!' % (name)

print( f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}' )

### list of formating specifications
# [[fill]align][sign][#][0][width][grouping_option][.precision][type]

### 1st example
print()

greet = 'WELCOME'
print( f'{greet:*<30}' )
print( f'{greet:*>30}' )
print( f'{greet:*^30}' )

### 2nd example
print()

total = 193181.19811651
debt = -1681.3185

pretty1 = (f'{total:+13,.2f} is your total.\n'
          f'{debt:+13,.2f} is your debt.')
pretty2 = (f'{total: =+13,.2f} is your total.\n'
          f'{debt: =+13,.2f} is your debt.')

print(pretty1)
print(pretty2)

### 3rd example
print()

twelve = 12

print( f'''\
Twelve in decimal is {twelve}
Twelve in binary is {twelve:#b}
Twelve in octal is {twelve:#o}
Twelve in hex is {twelve:#X}''' )

### 4th example
print()

upperCaseA = 65

print( f'{upperCaseA} as a character is {upperCaseA:c}' )

### 5th example
print()

grade = 76
total = 85

print( f'He got an {grade/total:.0%} on the test.' )
