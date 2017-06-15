nums = [10,21,1569,81,3,1,8,1,40,950,40,12,9,40,98,40,560,40,2,5,79,75,1010,65,68,41]

def filter_ints(int_list, filter):
    filtered = []
    for num in int_list:
        if filter(num):
            filtered.append(num)
    
    return filtered

# create another reference to the function
fltr = filter_ints

# creating filters using functions
def f_evens(number):
    return number % 2 == 0

def f_odds(number):
    return number % 2 == 1

# create filter using lambda
fl_evens = lambda n : n % 2 == 0

# pass those filters into the function
evens = fltr(nums, f_evens)
odds = filter_ints(nums, f_odds)

# pass in filters of lambdas
evens1 = fltr(nums, fl_evens)
evens2 = fltr(nums, lambda n : n % 2 == 0)
mul_three = fltr(nums, lambda a_number : a_number % 3 == 0)
everything = fltr(nums, lambda n : True)
tens = fltr(nums, lambda num : len(str(num)) == 2)

# these two are equivalent
def adder(a, b):
    return a + b

adder_l = lambda a, b : a + b

# calling a lambda immediately
is_div = (lambda n, d : n % d == 0)(9681681, 3) 

# lambda with no parameters
five = lambda: 5

val_five = five()
