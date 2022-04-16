# Saturday 16/4/22
#   for loops

# Suppose you want to check if London is in the most popular cities
city_to_check = "Birmingham"

# And you have assigned the 5 most popular cities to the list most_popular_cities
most_popular_cities = ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow"]

# This is one way to do it:
if city_to_check == most_popular_cities[0]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[1]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[2]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[3]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[4]:
    print("It's one of the most populated cities")

# But thats a lot of code
# Using a for loop is more convenient, it loops through the same steps
for popular_city in most_popular_cities:
    if city_to_check == popular_city:
        print("It's one of the most populated cities")

'''
 This code pulls each element in most_popular_cities, one by one.
 With each iteration, it assigns the current element to popular_city
 It then checks the value, so if "Edinburgh" is what we are checking, "Edinburgh" is assigned city_to_check
 Then after its been checked, if it is equal to "Birmingham", it will say: "It's one of the most populated cities"
'''

y = 2
z = 1

# The value after for keeps track of the value of the particular element being tested.
for x in y:
    if x == z:
        print("It's one of the most populated cities")

# Once Python finds a match, there is no point in continuing the loop, so use break:
for popular_city in most_popular_cities:
    if city_to_check == popular_city:
        print("It's one of the most populated cities")
        break