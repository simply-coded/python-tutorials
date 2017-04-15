
# create an empty set
a = set()

# create a set of items. the duplicates will automatically be removed
b = {13, 45, 23.3, 'test', 9, 45}

names = ['jake alfred', 'marry mavrich', 'lov milly', 'jake alfred', 'milherd mitch']

unames = set(names)

# common methods
unames.add('alice lakely')
unames.remove('lov milly')
person = unames.pop()
my_copy = unames.copy()

# clear set to None
unames.clear()

# convert string to set of characters
word1 = set('Jacob')
word2 = set('Malcom')

# word1 - word2
c = word1.difference(word2)

# word2 - word1
d = word2.difference(word1)

# word1 | word2
e = word1.union(word2)

# word1 & word2
f = word1.intersection(word2)

# word1 ^ word2
g = word1.symmetric_difference(word2)

# word1 = word1.union(word2)
word1.update(word2)

# word1 = word1.difference(word2)
word1.difference_update(word2)

# word1 = word1.intersection(word2)
word1.intersection_update(word2)

# word1 = word1.symmetric_difference(word2)
word1.symmetric_difference_update(word2)
