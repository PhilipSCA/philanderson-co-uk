# Tuesday 19/7/22
#   Accessing a dictionary of dictionaries

family_members = {
  "X": {
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  "Y": {
    "first name":"John",
    "last name":"Anderson.",
  },
  "Z": {
      "first name": "James",
      "last name": "Anderson"
  },
  "A": {
      "first name": "Philip",
      "last name": "Anderson" 
  },
  "B": {
      "first name": "Christa",
      "last name": "Anderson"
  }
}

# Previously we learnt how to find a value in a dictionary by specifying the key
print(family_members["Y"])
# This prints the whole dictionary of Y

# To find a specific value in the dictionary, you do this:
print(family_members["Y"]["first name"])