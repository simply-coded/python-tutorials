class Student:
    def __init__(self, fname, age, year):
        self.name = fname
        self.age = age
        self.year = year

    def last_name(self):
        return self.name.split(' ')[1]


stud1 = Student('Jake Miller', 17, 'Senior')
stud2 = Student('Alice Carry', 16, 'Junior')

print('Student one\'s last name is', stud1.last_name())
print('Student two is a', stud2.year)
