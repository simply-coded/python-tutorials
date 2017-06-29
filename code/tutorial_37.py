###
# video challenge answer
#
def get_money(customer, amount):              
    # calculate money needed to cover the "amount" to the nearest 5 dollar bill
    nonfive_bills = amount % 5
    remfive_bills = amount - nonfive_bills    
    needed = remfive_bills + (0 if nonfive_bills == 0 else 5)
    # take that money out of the customers wallet
    customer['wallet'] -= needed    
    # return the money you calculated to pay for the meal
    return needed

###
# factory functions
#
def make_is_divisble(den):

    def is_divisible(num):
        return num % den == 0

    return is_divisible

# create functions
is_div_2 = make_is_divisble(2)
is_div_13 = make_is_divisble(13)

# use them
a = is_div_2(12)
b = is_div_2(345+16122-48//45)
c = is_div_2(23*41981)

d = is_div_13(341)
e = is_div_13(5+12-48)
f = is_div_13(54*81)

# use it without saving the function
g = make_is_divisble(5)(1615)


###
# wrap existing functions
#
def whats_running(function):
    """Says when a function starts and stops.

    @usage
    your_function = whats_running(your_function)
    """

    def new_function():
        print(function.__name__, 'has started.')
        function()
        print(function.__name__, 'has stopped.')

    return new_function


def time_this(function):
    """Times a function in seconds.

    @usage
    your_function = time_this(your_function)
    """
    import time

    def wrapper(*args, **kargs):
        start = time.time()
        result = function(*args, **kargs)
        stop = time.time()
        print(f'{function.__name__} took {stop - start} seconds to execute.')
        return result

    wrapper.__name__ = function.__name__ + '_timed'
    return wrapper

# used for example functions
club = ['jake', 'alice', 'mark', 'john', 'jerry', 'kipper']

# example functions
def counter():
    for x in range(1_000_000):
        pass

def in_club(name, my_club=club):
    return name in my_club

# apply the wrapper functions
counter = time_this(counter)
in_club = time_this(in_club)

# you can apply a wrapper to an existing wrapped function
counter = whats_running(counter)

# call our newly wrapped functions
counter()

if in_club('jake'):
    print('They are in the club.')
else:
    print('They are not in the club.')

counter()
