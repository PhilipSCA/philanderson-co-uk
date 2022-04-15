# Friday 15/4/22
#    Popping Elements

tasks = ["check emails", "call Bob", "meet with Dylan"]
print(tasks)
# If you want to remove something from a list but keep it for another purpose, use ".pop"
# Say i just checked my emails and i wanted to add it to a list of completed tasks:
tasks_completed = tasks.pop(0)
print(tasks_completed)
# the value of the index number in the brackets is what gets popped
''' 
tasks[0] is "call Bob" and
tasks[1] is "meet with Dylan" and
tasks_completed is "check emails"
'''

# You can pop an element off a list and append it to another list
tasks_completed.append(tasks.pop(0))
print(tasks)

# You can also do the same but insert it instead of appending it.
tasks_completed.insert(2, tasks.pop(0))