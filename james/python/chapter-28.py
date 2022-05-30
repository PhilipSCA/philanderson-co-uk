# Thursday 26/5/22
#   The versatility of keys and values

# In the example we've been using, customer 115, the keys and values are strings.
customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

# But the keys dont have to be strings, they can be numbers.
customer_155_2 = {1: "James", 2: "Anderson", 3: "2203 random address"}

# To pick out a number, you do it like this:
# This would be "Anderson", its not like a list
customer_155_23 = customer_155_2[2]

# Values can be numbers aswell
customer_155_3 = {"first name": 1, "last name": 2, "address": 3}

# To pick out a value you do this
customer_155_32 = customer_155_3["last name"] # is 2

# You can mix the numbers any way you want, so you can put the key and value as numbers.

# When you have a dictionary with a lot of pairs, its easier to break it down.
customer_155_4 = {
    1: "James",
    "Anderson": 2,
    "address": "2203 random address",
    3: 2
}