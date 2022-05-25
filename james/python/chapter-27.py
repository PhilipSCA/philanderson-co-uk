# Wednesday 25/5/22
#   Accessing info in dictionaries

# If we use the same example, Customer 155, for this chapter, then there is 5 pairs of information
customer_115 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

# If we wanted to find a piece of information in a list, this is what we would do:
customer_info = customer_115[1]

# But in a dictionary, it is similar, except you pick out an element by specifying its key.
# This finds the value of "last name", which is "Anderson"
customer_last_name = customer_115["last name"]

# If you write
print(customer_last_name)
# It prints "Anderson"