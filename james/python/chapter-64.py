# Thursday 26/8/22
#   Retrieving data

# In the text file, greet.txt, its entire contents are the string "Hello, world!"
with open("greet.txt", "w") as f:
    f.write("Hello, world!")

# To retrieve those contents, we just use "r" for read instead of "w" for write.
with open("greet.txt", "r") as f:
    text_of_file = f.read()

# "Hello, world!" is now stored in text_of_file
print(text_of_file)