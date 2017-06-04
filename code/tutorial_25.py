names = ['jake', 'kate', 'alice', 'miller', 'bob']
grades = [80, 60, 46, 79, 96]

# example 1 - for each loop
for name in names:
    print(name + ', you are invited to my party.')

# example 2 - indexed loop
for index in range(0, len(names), 2):
    print(names[index] + ', you are invited to my party.')

# example 3 - testing range function outputs
test = range(2,4)
print('That range function would return:', list(test))

# example 4 - using else
test_char = 'e'
for char in 'Jeremy':
    if char == test_char:
        print('yes')
        break
else:
    print('no')

# example 5 - use a copy of your list if you are editing it
team = names
for person in team.copy():
    if person == 'kate':
        team.append('nick')

print(team)

# example 6 - loop through multiple lists
student_grades = dict()
for n, g in zip(names, grades):
    student_grades.update({n:g})

print(student_grades)

# example 7 - exiting a program
users = names
for tries in reversed(range(3)):
    current_user = input('Enter in your name: ')
    if current_user in users:
        break
    else:
        print('Incorrect. Tries left =', tries)
else:
    raise SystemExit

print('Welcome,', current_user)
