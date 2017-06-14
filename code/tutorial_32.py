import ctypes

def msgbox(message, title='', style=0):
    """Creates a message box for user input.

    Args:
        message (str)
        title (str)
        style (int)
            0 = OK
            1 = OK, Cancel
            2 = Abort, Retry, Ignore
            3 = Yes, No, Cancel
            4 = Yes, No
            5 = Retry, No
            6 = Cancel, Try Again, Continue
    Returns:
        1 = OK
        2 = Cancel
        3 = Abort
        4 = Retry
        5 = Ignore
        6 = Yes
        7 = No
        10 = Try Again
        11 = Continue
    """    
    return ctypes.windll.user32.MessageBoxW(0, message, title, style)


# get help with a function
print(msgbox.__doc__)
help(msgbox)

# basic usage
result = msgbox('Do you have a guitar?', style=4)
if result == 6:
    msgbox('Me too')
else:
    msgbox('Too bad')

# positional arguments
a = msgbox('Welcome to my program.', 'My Program:', 11)

# keyword arguments
b = msgbox(message='Running this program', style=2, title='Alert')

# unpack arguments
quest1 = ['Where you born in the US?', 'Questionnaire', 4]
quest2 = {'message': 'Are you male?', 'title': 'Questionnaire'}
quest3 = ('Is it rainy outside?', 'Questionnaire')

c = msgbox(*quest1)
d = msgbox(style=6, **quest2)
e = msgbox(*quest3, 5)

# arbitrary arguments
def output(*a_list):
    for item in a_list:
        print(item)

output('test', 1, 5, 65, 0, ['a', 'list'], 0, True, 'yup', 46810)

def output2(*a_list, sep_by=' '):
    for item in a_list:
        print(item, end=sep_by)

output2('test', 1, 5, 65, 0, ['a', 'list'], 0, True, 'yup', 46810, sep_by=';')

# arbitrary dictionary, to add optional extra fields
contact = []

def new_contact(addr_book, name, phone, addr, **extra_fields):
    info = {
        'name':name,
        'number':phone,
        'address':addr
    }
    for k, v in extra_fields.items():
        info[k] = v
    
    addr_book.append(info)
    
new_contact(contact, 'jeremy', 123415698, 'USA')
new_contact(contact, 'katelin', 45515698, 'USA', apt=1234, nickname='kate')

print( contact )
