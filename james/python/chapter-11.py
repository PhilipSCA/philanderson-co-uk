#  Saturday 9/4/22
    # Chapter 11: Else and elif statements

# In the if statements I did before, if it was false nothing happened.
drink = "Milk"
if drink == "water":
    print("Yep, its water")
if drink != "water":
    print("Nope, its not water")

# But a simpler way to do this is using 'else:' because if it isnt assigned water, of course its not water

if drink == "water":
    print("Yep, its water")
else:
    print("Nope, its not water")