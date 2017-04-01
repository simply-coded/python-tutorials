a_string = 'Test'

# create a list
my_list = [46511, 'stuff here', 12.31, a_string, 6]
grades = [98,55,46,68,81,88]

# get a specific item
a = grades[2]
b = grades[-4]

# get a range of items
c = grades[1:4]
d = grades[2:-1]
e = grades[-3:-1]

# leaving a side blank will represent the first or last indexes
f = grades[:3]
g = grades[1:]
h = grades[:]

# change values
grades[2] = 60
grades[3:5] = [30,81]

#repopulating list
grades = [98,55,46,68,81,88]

# delete 3rd index
grades[3:4] = []
del grades[3]

#repopulating list
grades = [98,55,46,68,81,88]

# delete 1st and 2nd items
grades[:2] = []
del grades[:2]

#repopulating list
grades = [98,55,46,68,81,88]

# delete the entire list
grades[:] = []
del grades[:]

# delete the variable pointing to the list
del grades

# splitting a string
name = 'Gabe Micer'
print( 'Initials are', name[0], name[5] )
print( name[0:4], f'{name[5]}.' )

# change a character in a string with concatenation
name = name[:6] + 'y' + name[7:]
print( name )

# change it back, by using a list
n_name = list(name)
n_name[6] = 'i'
name = ''.join(n_name)
print( name )
