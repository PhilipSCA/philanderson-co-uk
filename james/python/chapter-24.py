# Saturday 21/5/22
#   Changing case

# A list of the most popular cities in the UK
most_popular_cities = ["London", "Edinburgh", "Manchester", "Birmingham", "Liverpool", "Glasgow"]

# If someone enters "london" instead of "London", python wont count it
# Here is how to make python read lower case too, or any different capitals
# because even if we just do lower case, "loNDOn" wont work.

city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
most_popular_cities = ["london", "edinburgh", "manchester", "birmingham", "liverpool", "glasgow"]
for a_popular_city in most_popular_cities:
    if city_to_check == a_popular_city:
        print("Its one of the most populated cities!")

# If you use .title, you can change "london" back into "London"
city_to_check = city_to_check.title
