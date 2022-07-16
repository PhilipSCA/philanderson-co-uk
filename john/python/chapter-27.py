date = "Saturday 16/07/22"
print(date)

customer_29 = {"first name": "David", "last name": "Elliot", "address": "4308 Wellesley St."}

address_of_customer = customer_29["address"]
print(address_of_customer)
# keys dont have to be strings, they can be numbers
rankings = {5: "Finland", 2: "Norway", 3: "Sweden", 7:"Iceland"}
second_ranked_country = rankings[2]
print(second_ranked_country)

country_rankings = {"Finland": 5, "Norway": 2, "Sweden": 3, "Iceland": 7}
norway_rank = country_rankings["Norway"]
print(norway_rank)

# it is better to write it like this:
rankings = {
    5: "Finland",
    2: "Norway", 
    3: "Sweden", 
    7: "Iceland",
}