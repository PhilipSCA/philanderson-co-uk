# Wednesday 13/4/22
#   Chapter 16: Adding, changing list elements

cities = ["London", "Manchester", "Liverpool", "Bristol", "Birmingham"]

# Suppose you want to add a six element, this is the code:
cities.append("Leeds")

# The code above adds Leeds on to the end of the list
# cities[5] is assigned "Leeds"

# If your adding a number instead of a string, no quotation marks needed
# scores.append(47)

# This is an alternative way to append.
cities = cities + ["Cambridge", "Sheffield"]

# You can add a list onto an existing list
longer_list_of_cities = cities + ["Cambridge", "Sheffield"]

# You can create an empty list by putting nothing in the brackets
cities2 = []

# If you want to insert an element anywhere in the list, you do this:
cities.insert(2, "Newcastle")
# Here I inserted it into the third place
# The element in the third place (Liverpool) that got replaced moves down to cities[3]