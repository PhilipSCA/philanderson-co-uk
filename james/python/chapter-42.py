# Thursday 21/7/22
#   Passing functions information

def add_numbers():
    first_number = 2
    second_number = 3
    total = first_number + second_number
    print(total)

# To call a function, you just do this
add_numbers()

# The parenthesis dont have to be empty
# Now your passing data as well as calling the function
# The numbers inside the parenthesis are called arguments
add_numbers(50, 40)

# In this, "first_number" is 50
# And "second_number" is 40
# The variables inside the parenthesis here are called parameters, which hold arguments.
def add_numbers(first_number, second_number):
    total = first_number + second_number
    print(total)

# total = 90

# You can put a variable into the parenthesis too.
def greet_user(greeting):
    print(greeting)

greeting = "Hello there"
greet_user(greeting)


