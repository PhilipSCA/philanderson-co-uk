# Saturday 25/6/22
#   Looping through dictionary key-value pairs

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

# # Last chapter we learnt how to loop through dictionary keys (first name , last name, etc)
# This chapter is looping the dictionary key-value pairs (first name is James, etc)
# Its simple, its just the same thing, but swap key for value

for each_key, each_value in customer_155.items():
    print("The customer's " + each_key + " is " + each_value)