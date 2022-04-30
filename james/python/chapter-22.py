# Saturday 30/4/22
#   for loops nested

# Say you had a list of first names and last names
first_names = ["James", "John", "Peter", "Andrew", "Matthew"]
last_names = ["Anderson", "Coles", "Parker", "Smith"]

# In total there could be 20 different combinations of names
# Starting with James we go through all the possible names
name1 = "James Anderson"
name2 = "James Coles"
name3 = "James Parker"
name4 = "James Smith"

# and if you did this for every name, there would be 20 combinations

# Python can do the repetitive work using nested for statements
first_names = ["James", "John", "Peter", "Andrew", "Matthew"]
last_names = ["Anderson", "Coles", "Parker", "Smith"]
full_names = []
for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)
    
print(full_names)