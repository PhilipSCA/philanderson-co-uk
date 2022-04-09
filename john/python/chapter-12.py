date = "Friday 08/04/22"
print(date)

weight = 300
time = 6
if weight <= 300 and time <= 6:
    status = "try to recruit him"
    print(status)

salary = 52000
bonus = 11000
has_a_lamborghini = "yes"

if salary > 60000 or bonus > 10000 or has_a_lamborghini == "yes":
    wealth = "rich"

if (salary < 60000 and bonus < 10000) or has_a_lamborghini == "no":
    wealth = "not rich"


print("he is " + wealth)