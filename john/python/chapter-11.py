date = "Friday 08/04/22"
print(date)

species = "dog"
if species == "cat":
    print("Yep, its cat.")
if species != "cat":
    print("Nope, not cat.")
# the easier way is using else:
if species == "cat":
    print("Yep, its cat.")
else:
    print("Nope, not cat.")



donut_condition = "not fresh" 
donut_price = "low"

buy_score = 0
if donut_condition == "fresh":
    buy_score += 10
elif donut_price == "low":
    buy_score += 5
print("buy score is " + str(buy_score))
