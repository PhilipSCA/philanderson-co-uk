#  Saturday 9/4/22
    # Chapter 11: Else and elif statements

# In the if statements I did before, if it was false nothing happened.
drink = "milk"
if drink == "water":
    print("Yep, its water")
if drink != "water":
    print("Nope, its not water")
    
# But a simpler way to do this is using 'else:' because if it isnt assigned water, of course its not water.

if drink == "water":
    print("Yep, its water")
else:
    print("Nope, its not water")

# Finally, there's 'elif'. Its short for 'else if'. If no test has been successful, elif tries something else.

if drink == "water":
    print("Yep, its water")
elif drink == "milk":
    print("Oh, its actually milk")
else:
    print("Nope, its not water or milk")

# You can have any number of elif statements.
# You would never have any more than one else statement as its at the end.

# If you dont want to stop testing even after one is successful, you just keep using if.
if drink == "water":
    print("Yep, its water")
if drink == "milk":
    print("Oh, its actually milk")
if drink == "juice":
    print("Nope, its not water or milk")