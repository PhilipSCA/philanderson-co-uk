# Saturday 25/6/22
#   Looping through dictionary values

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
# Lets say you wanted to display all the values in the customer_155 dictionary
print(customer_155["first name"])
print(customer_155["last name"])
print(customer_155["address"])
# This would show:
# James
# Anderson
# 2203 random address

# This works but imagine a much longer dictionary, it would be too long to write them all out.
# This is why you use looping
for each_value in customer_155.values():
    print (each_value)


