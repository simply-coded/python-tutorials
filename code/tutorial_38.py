# -------------------------------------------------------------------------------------------
def time_this(func):    
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        r_value = func(*args, **kwargs)
        stop = time.time()
        runtime = stop - start
        print(f'{func.__name__} took {runtime} seconds to exeucte.')
        return r_value
    
    wrapper.__name__ = func.__name__ + '_timed'
    return wrapper


@ time_this
def sum_to_1(stop):
    total = 0
    for n in range(1, stop + 1):
        total += n

    return total

# decorator @time_this is the same as
sum_to_1 = time_this(sum_to_1)

result_1 = sum_to_1(30)

print(result_1)


# -------------------------------------------------------------------------------------------
def make_time_this(allowed=10):

    def time_this(func):    
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            r_value = func(*args, **kwargs)
            stop = time.time()
            runtime = stop - start
            if runtime > allowed:
                print(f'{func.__name__} took {runtime} seconds to exeucte. You might want to optimize it.')

            return r_value
        
        wrapper.__name__ = func.__name__ + '_timed'
        return wrapper

    return time_this

@ make_time_this(1)
def sum_to_2(stop):
    total = 0
    for n in range(1, stop + 1):
        total += n

    return total

# decorator @make_time_this(1) is the same as
sum_to_2 = make_time_this(1)(sum_to_2)

# probably won't tell the time it took to execute (depends on your computer speed)
result_2 = sum_to_2(30)

print(result_2)

# probably will tell how long it took to exeucte (depends on your computer speed)
print(sum_to_2(20_000_000))


# Some simpler examples that don't make sense but is allowed.
# -------------------------------------------------------------------------------------------
# use regular factory function ( this is normal )
def make_greet_1():
    
    def greet(name):
        print('hello there', name)

    return greet


test_1 = make_greet_1()
test_1('jeremy')

# -------------------------------------------------------------------------------------------
# use decorator which inputs the current function, despite not using the inputed function ( not normal )
def make_greet_2(function):
    
    def greet(name):
        print('hello there', name)

    return greet

@ make_greet_2
def test_2():
    pass

test_2('jeremy')

# -------------------------------------------------------------------------------------------
# another case of using a decorator which inputs the current function, despite not using it
def change_func_to_int(function):
    return 5    

@ change_func_to_int
def test_3():
    pass

# no longer a function. just prints out 5
print(test_3)
