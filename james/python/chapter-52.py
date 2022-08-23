# Tuesday 23/8/22
#   Setting a flag
most_populated_cities = ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow"]
# We learnt to use a while loop to keep repeating something until the user stops it or something is recognised.

user_input = ""
while user_input != "ESC":
    user_input = input("Enter a city, or ESC to quit:")
    if user_input != "ESC":
        for a_populated_city in most_populated_cities:
            if user_input == a_populated_city:
                print("It's one of the most populated cities")
                break

# Im going to modify this code to use a flag.
keep_looping = True
while keep_looping == True:
    user_input = input("Enter a city, or ESC to quit.")
    if user_input != "ESC":
        for a_populated_city in most_populated_cities:
            if user_input == a_populated_city:
                print("It's one of the most populated cities")
                break
    else:
        keep_looping = False

# Line 17 says as long as keep_looping says True, keep looping.
# Line 24 and 25 say if the user entered Esc, change keep_looping to False, so stop looping.