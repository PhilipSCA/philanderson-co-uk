# Saturday 9/4/22
    # Testing sets of conditions

# You can test for a combination of conditions by using 'and'.
temp = 15
people = 500000
parent = "alum"
if temp > 30 and people < 100000:
    status = "Very crowded outside"

# If only one of the conditions is met, it fails. It has to be both.
# You can chain any number of conditions together
weight = 356
time = 5.2
age = 35
height = 78
res = "U.K"
if weight > 300 and time < 6 and age > 17 and height > 72:
    status = "Try and recruit him"

# You can also create a test that passes if any condition is met using 'or'.
if temp > 30 or people < 515300 or parent == "alum":
    message = "Welcome to Leeds Beach!"

# You can combine any number of 'and' and 'or' conditions. These create ambiguties
if age > 65 or age < 21 and res == "U.K":
    print("Just needed this for no error")

# This can be read in two ways:
# If the person is over 65 or under 21, and is a resident of the UK, its true
# If the person is over 65, and under 21 or a resident of the UK, its true

# You fix this the same way with maths, using brackets
if (age > 65 or age < 21) and res == "U.K":
    print("Just needed this for no error")
    # or
if age > 65 or (age < 21 and res == "U.K"):
    print("Just needed this for no error")