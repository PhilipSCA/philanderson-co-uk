# Saturday 25/6/22
#   Removing and changing dictionary items

# If you remember how to delete an element from a list, its like this:
customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
del customer_155[0]

# To delete a key-value pair from a dictionary:
del customer_155["last name"]

# To change the value in a dictionary:
customer_155[2] = "Smith"
#or
customer_155["first name"] = "John"