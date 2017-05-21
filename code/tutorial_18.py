jake_age = 15
anne_age = 17

# are they the same age?
same_age = jake_age == anne_age

# are they different ages?
diff_age = jake_age != anne_age

# is jake younger / anne older
jake_younger = jake_age < anne_age

# is jake older / anne younger
anne_younger = jake_age > anne_age

# can also check greater than or equal, and less than or equal
print( jake_age <= 15 )
print( jake_age < 15 )

# notice the order doesn't matter as long as the logic is correct
print( 17 >= anne_age )
print( 17 > anne_age )

# compare lists, tuples, strings
print( 'a' < 'd' )
print( 'z' < 'd' )
print( 'cat' > 'cop' )

# compares: 80 > 80 or 70 > 65
print( [80,70,90] > [80,65] )

# compares: 'hello' == 'Hello' and 'there' == 'there'
# if the lengths don't match it will always be false.
print( ('hello', 'there') == ('Hello', 'there') )
