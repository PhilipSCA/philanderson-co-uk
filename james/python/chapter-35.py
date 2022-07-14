# Thursday 14/7/22
#   Accessing a list of dictionaries

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

# To get information out of a dictionary you do this:
customer_155_first_name = customer_155["first name"]

# But when we have a list, the dictionaries have no name
# Instead they have id's (Hannah's index number is 0), but I can give her any family id I want

family_members = [
  {
    "family id": 0,
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  {
    "family id": 1,
    "first name":"John",
    "last name":"Anderson.",
  }
  {
    "family id": 2,
    "first name":"James"
    "last name":"Anderson."
  },
  {
    "family id": 3,
    "first name":"Philip"
    "last name":"Anderson."
  },
  {
    "family id": 4,
    "first name":"Christa"
    "last name":"Anderson."
  },
] 

# If I want to know the address of a customer whose id is 1000. This is the code:
dictionary_to_look_in = family_members[1000]
family_members_address = dictionary_to_look_in["address"]