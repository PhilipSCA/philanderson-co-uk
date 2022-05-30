# Monday 30/5/22
#   Adding items to dictionaries

# If we use the same example - Customer 155, these are the current values
customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

# You can add a new pair by writing:
# There are a lot of similar pieces to other things you can do, just in a different order
customer_155["city"] = "London"

# Now Customer 155's values are
customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address", "city": "London"}

# In the previous chapter, you learnt how to define a dictionary by breaking it down:
customer_155_2 = {
    1: "James",
    "Anderson": 2,
    "address": "2203 random address",
    3: 2
}

# You can define an empty dictionary like this too:
customer_155_3 = {}
# Then you can fill it later with keys and values
customer_155_3[1] = "James"
customer_155_3["Anderson"] = 2
customer_155_3["address"] = "2203 random address"