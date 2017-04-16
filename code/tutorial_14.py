
# empty dictionary 
a = {}

# simple dictionary
b = {'f_name': 'Jeremy', 'l_name': 'England', 'fav_num': 9} 

# get an item
last_name = b['l_name']

# change an item
b['f_name'] = 'Jeremiah'

# delete an item
del b['fav_num']

# different ways to add an item
b.update({'phone': 123456789})
b.update(address='1234 Nope Lane, USA')
b.update([('age', 97)])

# dictionary, and list as values
grades = {
    'Jake': {'Exam 1': 78, 'Exam 2': 90, 'Quiz 1': 89},
    'Alice':[99,98,79,65]
}

# add new person 
grades.update(Kyle={'Exam 1': 80, 'Exam 2': 87, 'Quiz 1': 96})

# change alice from a list to a nested dictionary 
grades['Alice'] = {'Exam 1': 97, 'Exam 2': 67, 'Quiz 1': 93}

# get a grade
quiz1 = grades['Jake']['Quiz 1']
