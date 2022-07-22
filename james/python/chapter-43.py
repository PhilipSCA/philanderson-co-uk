# Friday 22/7/22
#   Passing functions information differently

# Before the arguments were positional arguments
# They had to be put in order to match the parameter

def add_numbers(first_number, second_number):
    total = first_number + second_number
    print(total)

add_numbers(50,40)

# 50 is the first_number
# 40 is second_number

# But you dont have to make it like this
# These are keyword arguments, the order doesnt matter
def names_of_siblings(brother_name, sister_name):
    print("The names of the siblings are " + brother_name + " and " + sister_name)

names_of_siblings(brother_name="James", sister_name="Hannah")

# Python displays: The names of the siblings are James and Hannah.

# If you reverse it, it will be the same
def names_of_siblings(sister_name, brother_name):
    print("The names of the siblings are " + sister_name + " and " + brother_name)

names_of_siblings(brother_name="James", sister_name="Hannah")