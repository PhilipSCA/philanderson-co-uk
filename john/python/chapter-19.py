date = "Saturday 25/06/22"
print(date)

tasks = ["email Frank", "call Sarah", "meet with Zach"]
latest_task_done = tasks.pop(1)
print(tasks)
# if you want to remove call sarah from this list and put in it another list:
tasks_done = []
tasks_done.append(latest_task_done)
print(tasks_done)
# Or do it quicker this way
tasks_done.append(tasks.pop(1))