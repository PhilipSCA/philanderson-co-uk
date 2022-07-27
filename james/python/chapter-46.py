# Wednesday 27/7/22
#   An unknown number of arguments

def display_result(winner, score):
    print("The winner was " + winner)
    print("The score was " + score)

display_result(winner="Liverpool", score="2-0")

# But say you want to display other information if something happens.
display_result(winner="Liverpool", score="2-0", overtime="yes", injuries="none")

# The function can handle optional arguments with this code:
def display_result(winner, score, **other_info):
    print(display_result)

# The two astericks followed by a parameter mean that there may or may not be one or more arguments passed.
# It makes the parameter a dictionary

other_info = {"overtime": "yes", "injuries": "none"}

# This is just there to make other_info mean something

def display_result(winner, score):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)

# For positional optional arguments, you just put one asterick.
def display_nums(first_num, second_num, *opt_nums):
    print(first_num, second_num, opt_nums)

display_nums(100, 200, 300, 400, 500)


