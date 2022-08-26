# Thursday 26/8/22
#   Appending data

# To append data to a file while preserving existing data in the file, you write:
with open("greet.txt", "a") as f:
    f.write("\nHave a nice day")

# the \n makes a new line, so the text that follows is placed on a new line.
# If I write:
with open("greet.txt") as f:
    message = f.read()
    print(message)

# Python displays
# "Hello world!"
# "Have a nice day"