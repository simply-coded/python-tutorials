students = {
    'tom': [80, 60, 75, 63],
    'kate': [20, 89, 62, 80, -56],
    'bill': [89, 57, 48, 60, 103]
}

names = {
    'longer': 'jake',
    'noodlehead': 'kimley',
    'crutcher': 'ally'
}

# ex 1 - nested for loop
for grades in students.values():
    for grade in grades:
        print(grade)

# ex 2 - comprehensive list. add 3 to scores below 70
students['tom'] = [(g + 3 if g < 70 else g) for g in students['tom']]

# ex 3 - nested comprehensive list. get all valid grades
all_grades = [g for grades in students.values() for g in grades if g >= 0 and g <= 100]
class_avg = sum(all_grades) / len(all_grades)

print(class_avg)

# ex 4 - comprehensive sets
print( { char for char in 'Je1re2my' if not char.isdigit() } )

# ex 5 - comprehensive dictionaries
switcheroo = {first:last for first, last in zip(names.values(), names.keys())}

print(switcheroo)
