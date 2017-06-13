names = ['mark', 'nia', 'kate', 'jenny', 'kate']
scores = [90, 80, 65, 87, 90, 60, 68, 78, 91, 90, 63, 64]

index = 3

def nth_index(lst, occur, search_for):            
    curr_i = 0
    for x in range(occur):
        curr_i = lst.index(search_for, curr_i)
        index = curr_i
        curr_i += 1    
    return index

# call my method and get the result
found_i = nth_index(names, 2, 'kate')

# you get to choose whether or not to override index
index = found_i

# use the information that my method returned
names[index] = 'katy'

# returning different values depending on the situation
def birthday(age):
    if is_dead:
        return age    
    return (age + 1)

# test the function
is_dead = False
print( birthday(87) )

is_dead = True
# test the alternative result
print( birthday(87) )

# return None to stop a function
def greet(name):
    if name not in names:
        return
    print('Welcome,', name)


# this will not display anything
greet('jeremy')

# this will display the greeting
greet('nia')

# return multiple values
def is_div(num, div1, div2):    
    res1 = num % div1 == 0
    res2 = num % div2 == 0
    return res1, res2 
        
# return them both into one variable
result = is_div(80, 4, 3)

is_div_by4 = result[0]
is_div_by2 = result[1]

# unpack tuple into variables
is_div_by21, is_div_by5 = is_div(106510, 21, 5)

# split before returning
is_div_by9 = is_div(540, 3, 9)[-1]
