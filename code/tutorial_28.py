import sys

# save the args list into a variable
args = sys.argv

# get an argument. first arg will always be the python file itself
first_arg = args[0]

# loop through all user added arguments
for arg in args[1:]:
    print(arg)

# sum up args that are digits
if len(args) > 1:
    total = sum(int(arg) for arg in args[1:] if arg.isdigit())
    print('Total is', total)
else:
    print('No integer arguments provided to add up.')
