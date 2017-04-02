# create two lists
list1 = ['cat', 'dog', 'mouse', 'bird']
list2 = ['ape', 'lizard', 'mouse']

# concatenate/combine lists together
animals = list1 + list2 + ['horse', 'croc']

# add a single item to a list
animals.append('frog')

# find out at what index a value occurs
found1 = f'Mouse found at {animals.index("mouse")}'

# find the second occurrence of a value
found2 = f'Mouse also at {animals.index("mouse", animals.index("mouse") + 1)}'

# remove first occurrence of 'mouse'
animals.remove('mouse')

# insert 'fish' at index 2
animals.insert(2, 'fish')

# remove and retrieve the last item of the list
last_item = 'Here is the last item in the list: ' + animals.pop()

# sort alphabetically
animals.sort()

# reverse the order of the list
animals.reverse()

# make a copy of the list
animals2 = animals.copy()

# clear the list
animals.clear()

# create nested list
grades = [ 
    ['Jack',80,90,88,74],
    ['Alice',56,40,99,70],
    ['Kate',90,98,97] 
]

# get and store data from the nested list
s1_name = grades[0][0]
s1_grades = grades[0][1:]

s2_name = grades[1][0]
s2_grades = grades[1][1:]

s3_name = grades[2][0]
s3_grades = grades[2][1:]

# add a student using concatenation
grades = grades + [['Bill',80,60,55,74]]

# add a student with a method
grades.append(['Cherol',10,54,64,84])

# create a string of character
characters = 'qwertuiopasdghjklxcvbn!m'

# split into list, and sort alphabetically
sa_list = sorted(characters)

# remove unwanted characters
sa_list.remove('!')

# add missing character inside of the list
sa_list[4:5] = [ sa_list[4], 'f' ]

# add missing character the easy way
sa_list.insert(5, 'f')

# add characters at end of list
sa_list[-1:] = [ sa_list[-1], 'y', 'z']

# add characters at end of list the easy way
sa_list = sa_list + ['y', 'z']
