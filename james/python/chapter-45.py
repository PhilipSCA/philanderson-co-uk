# Monday 25/7/22
#   Mixing positional and keyword arguments

def give_greeting(greeting, first_name):
    print(greeting + ", " + first_name)

# First argument is positional, second is keyword
give_greeting("Hello there", first_name="Al")

# Python displays "Hello there, Al"

# Key things:

# Positional arguments must come before keyword arguments
# Positional arguments have to line up with parameters, the keyword argument cant be in its place.

def give_greeting(greeting, first_name, nickname=" the magic boy"):
    print(greeting + ", " + first_name + nickname)

# Positional arguments first
# Keyword arguments with no default second
# Keyword arguments with a default last.

# Lists and dictionaries can be arguments
family_members = {
  "X": {
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  "Y": {
    "first name":"John",
    "last name":"Anderson.",
  },
  "Z": {
      "first name": "James",
      "last name": "Anderson"
  },
  "A": {
      "first name": "Philip",
      "last name": "Anderson" 
  },
  "B": {
      "first name": "Christa",
      "last name": "Anderson"
  }
}

def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])

# The function uses three parameters to find the value we want:
find_something(family_members, "Y", "first name")

# Python displays:
# John