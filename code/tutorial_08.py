#print( 'c:\users\jeremy\desktop' ) error
print( r'c:\users\jeremy\desktop' ) #removes backslash \ meaning

name = 'Larry'
age = 44

# concatenation
a = name + ' is ' + str(age) + ' years old.'

# formatted string
b = f'{name} is {age} years old.'

# using variable more than once
c = F"{name} is {age} years old. {name}'s very tall."

# formatted string function
d = '{} is {} years old.'.format(name, age)

# same thing as above
e = '{0} is {1} years old.'.format(name, age)

# changing order
e = '{1} is {0} years old.'.format(name, age)

# using a variable more than once.
f = "{0} is {1} years old. {0}'s very tall.".format(name, age)

# naming your placeholders.
g = "{first_name}'s number is {phone_number}.".format(phone_number=123456789, first_name=name)

# type formatting
h = "My name is %s, and I've been walking for %d miles. Could you spare some change. All I need is $%.2f for a meal." % ('Max', 23, 6.43878)
