date = "Saturday 25/06/22"
print(date)

tasks = ["email Frank", "call Sarah", "meet with Zach"]
del tasks[0]
print(tasks)

tasks2 = ["email Frank", "call Sarah", "meet with Zach"]
del tasks[1]
# tasks2 is now "email frank" and "meet with Zach"

# you can also use .remove

tasks.remove("email Frank")
print(tasks)