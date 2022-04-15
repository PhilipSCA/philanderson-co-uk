# Thursday 14/2/22
#    Deleting and removing elements

# Say you have a list of tasks to do
tasks = ["check emails", "call Bob", "meet with Dylan"]
print(tasks)
# tasks[0] is "clean sink"

# To strike elements off the list, you write:
del tasks[0]
# tasks[0] is now "call Bob", because "clean sink" was removed.

print("This is tasks without the first element, clean sink")
print(tasks)

# You can delete any list element by just specifying the index number
del tasks[1]
# tasks[1] is now "meet with Dylan"

print("This is tasks without the second element, call Bob")
print(tasks)

# An alternative way to delete elements from lists:
tasks.remove("call Sarah")