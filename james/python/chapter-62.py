# Thursday 25/8/22
#   Data files

# If we put all the things we've done on a computer, when it turns off, it would all be deleted.
# This is how to begin to save data processed by python
with open("whatever.txt", "w") as file_to_work_with:

# This line opens the text file whatever.txt if it exists.
# If it doesnt exist, Python creates it.

# You could open the file without the initial with, opting to close the file yourself.
file_to_work_with = open("whatever.txt", "w"):

# The designation "whatever.txt" assumes that the file is in the same folder as the Python program.
# If it isnt in the same folder, e.g if its in the data subfolder of the Python folder on Windows, you write:
with open("data\whatever.txt", "w") as file_to_work_with:

# On OS(Apple) and Linux, you use a forward slash:
with open("data/whatever.txt", "w") as file_to_work_with:

# The variable file_to_work_with can be anything, as long as its legal.