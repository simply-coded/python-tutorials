
shopping_list = [
    'milk','eggs','bacon','beef',
    'soup','bread','mustard','toothpaste'
    ]

# looping by index vs using an iterator
i = 0
while i < len(shopping_list):
    curr_item = shopping_list[i]
    print( curr_item )
    i += 1

for curr_item in shopping_list:
    print( curr_item )

#shopping_list.__iter__()
pencil_holder = iter(shopping_list)

#pencil_holder.__next__()
first = next(pencil_holder)
sec = next(pencil_holder)

print( first, sec )

# very large generator expression
pow_three = (n ** 3 for n in range(1000000000000))

# if you used a list comprehension you'd most likely run out of memory.
 #pow_three = [n ** 3 for n in range(1000000000)]

# the generator will only calculate the first 10 powers of three and then pause until you use next() again
for t in range(10):
    print(t, next(pow_three) )

# prints out the eleventh power of 3
print( next(pow_three) )

# use generators to create previous comprehensions
pow_four = tuple(n ** 4 for n in range(10))
pow_five = list(n ** 5 for n in range(10))
pow_six = set(n ** 6 for n in range(10))
pow_sev = dict( (n, n ** 7) for n in range(10))
