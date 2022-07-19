# Monday 18/7/22
#   Creating a dictionary of dictionaries

# Instead of a list of dictionaries, have a dictionary of dictionaries
# This is the list of dictionaries we had earlier, there are 5 dictionaries with 3 key-value pairs
family_members = [
  {
    "family id": 0,
    "first name":"Hannah",
    "last name":"Anderson."
  },
  {
    "family id": 1,
    "first name":"John",
    "last name":"Anderson."
  },
  {
    "family id": 2,
    "first name":"James",
    "last name":"Anderson."
  },
  {
    "family id": 3,
    "first name":"Philip",
    "last name":"Anderson."
  },
  {
    "family id": 4,
    "first name":"Christa",
    "last name":"Anderson."
  },
] 

# To create a list of dictionaries, do this

family_members = {
  0: {
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  1: {
    "first name":"John",
    "last name":"Anderson.",
  },
  2: {
    "first name": "James",
    "last name": "Anderson"
  },
  3: {
    "first name":"Philip",
    "last name":"Anderson."
  },
  4: {
    "first name":"Christa",
    "last name":"Anderson."
  },
}

# The dictionary names dont have to be numbers though, you can make them any string.

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
    "first name":"Philip",
    "last name":"Anderson."
  },
  "B": {
    "first name":"Christa",
    "last name":"Anderson."
  },
}