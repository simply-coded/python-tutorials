first = 'Alice'
last = 'Pringtin'
visited = 0

def greet():  
    global last, visited
    first = 'Mark'
    last = 'Pringston'
    visited += 1  
    print('=============================')
    print(f'Welcome, {first} {last}')
    print('Glad to have you.')
    print('Times visited =', visited)
    print('-----------------------------')

greet()
greet()

print('Global variables "last", and "visited" are now:', last, visited)
print('Global variable "first" has not changed:', first)
