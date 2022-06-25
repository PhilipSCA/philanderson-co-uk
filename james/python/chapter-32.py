# Saturday 25/6/22
#   Looping through dictionary keys

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

# Last chapter we learnt how to loop through dictionary values (James, Anderson, etc)
# This chapter is looping the dictionary keys (first name , last name, etc)
# Its simple, its just the same thing, but swap key for value

for each_key in customer_155.keys():
    print(each_key)