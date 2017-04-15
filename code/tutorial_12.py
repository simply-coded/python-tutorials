# empty tuple
a = ()

# one item tuple
b = 43,

# preferable to use parenthesis around tuples
b = (43,)

# multiple items in a tuple
c = 'sting', 12, 13.5, 'test', [12, 'ok'], (33, 21)
c = ( 'sting', 12, 13.5, 'test', [12, 'ok'], (33, 21) )

# get an item from a tuple
print( c[0] )

# get a range from a tuple
print( c[2:5] )

# unpacking a sequence data types
grades = [84, 93, 30, 94]
grade1, grade2, grade3, grade4 = grades
print('Second test score is', grade2)

# create a tuple from a list
report = tuple(grades)


# unpacking a complex range of data
students = ( 
    ('Jake', [90,80,75,78,84,100]),
    ('Amy', [72,65,98,58,45,77]),
    ('Merry', [91,93,100,98,94,89]),
)

# get first two students
st1, st2 = students[:2]
print(st1, st2)

#get their last two grades
st1_grades, st2_grades = st1[1][4:], st2[1][4:]

print(st1[0], 'last two grades are', st1_grades)
print(st2[0], 'last two grades are', st2_grades)

# combine three tuples
names = ('jake',)
a_names = ('alice', 'anne')
b_names = ('ben', 'belomy')
names = a_names + b_names + names

print(names)
