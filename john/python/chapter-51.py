from distutils.command.clean import clean


date = "Thursday 25/08/22"
print(date)
#27 lines

# While Loops

# This is a for loop, it checks one thing and sees if its on the list.
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
city_to_check = input("Enter the name of a city: ")
for a_clean_city in cleanest_cities:
      if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")
      break

# This is a while loop. The difference is this allows the user to check another city after another or stop by pressing "q". If
user_input = ""
while user_input != "q":
  user_input = input("Enter a city, or q to quit:")
  if user_input != "q":
    for a_clean_city in cleanest_cities:
      if user_input == a_clean_city:
        print("It's one of the cleanest cities")
      break