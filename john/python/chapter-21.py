date = "Wednesday 13/07/22"
print(date)

city_to_check = "Tucson"

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]

for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("Its one of the cleanest cities")
        break