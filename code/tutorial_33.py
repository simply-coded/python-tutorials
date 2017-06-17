def loop_str(string):
    for char in string:
        yield char

def count():
    c = 1
    while True:
        yield c
        c += 1

def countTo(limit):
    c = 1
    while c <= limit:
        yield c
        c += 1

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def fibTo(limit):
    a, b = 0, 1
    for x in range(limit):
        yield b
        a, b = b, a + b

# usage examples
get_chars = loop_str('Hello There')

# call next to get the value that is yielded
char_1 = next(get_chars)

# next is automatically called in for loops
print( [num for num in countTo(23)] )

# generators remember where they left off
char_2 = next(get_chars)

# using a generator here saves us memory because we don't 
# have to create all 30 fibonacci numbers, just the first 9
for n in fibTo(30):  
    if n == 55:
        break          
    print(n)

# we can create new generators from the same function
get_chars_2 = loop_str('Something else.')
first_char = next(get_chars_2)

# and it won't mess up the current ones we have going
char_3 = next(get_chars)
