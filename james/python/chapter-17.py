# Thursday 14/2/22
#    Taking slices from lists

cities = ["London", "Manchester", "Liverpool", "Bristol", "Birmingham"]

# You can copy elements in the list to create a smaller list
smaller_list_of_cities = cities[1:4]

# With this you end up with "Manchester", "Liverpool" and "Bristol" in smaller_list_of_cities

# When you slice from a list, you copy a part of it, not cut
# The first number targets the first element in the slice
# The number after the colon is the index number that comes after the last element in the slice.
# So if you want the last element in the slice to be index number 4, you put 5

# When the first element of the slice is the first element in the list, you can leave out the first number:
smaller_list_of_cities2 = cities[:4]

# When the last element of the slice is the last element in the list, you can leave out the last number
smaller_list_of_cities3 = cities[1:]

print(cities)
print(smaller_list_of_cities)
print(smaller_list_of_cities2)
print(smaller_list_of_cities3)