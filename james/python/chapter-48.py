# Monday 8/8/22
#   Functions as variables

# A function IS a variable
def sum(first_number, second_number):
    return first_number + second_number

def subtract(first_number2, second_number2):
    return first_number2 - second_number2

sum_result = sum(1, 2)
subtract_result = subtract(3, 2)
overall_result = sum_result + subtract_result
# overall_result = 4 (1 + 2 = 3 | 3 - 2 = 1. (3 + 1 = 4))

# This code can be shortened by putting the functions in the variables place

overall_result = sum(1, 2) + subtract(3, 2)